import argparse
import os
import shutil
import numpy as np
import json
import cv2
from PIL import Image

"""
A playground method to see the details of the annotation for object detection task.
It is possible to obtain more information from the .json file according to coco format.
However, since the computer vision challenge we are dealing with is Object Detection then the only the information required 
for the object detection task such as class id and coordinates of bounding box, only those are to be displayed in this method. 
display_annotation_sample('0027_Z_coco.json')
"""
def display_annotation_sample(annotationFileName):
    f = open(annotationFileName)
    data = json.load(f)
    imageID=0
    for i, ann in enumerate(data['annotations']):   
        if ann['image_id'] == 250:
            imageID=ann['image_id']
            print(ann['category_id'], ann['bbox'][0], ann['bbox'][1], ann['bbox'][2], ann['bbox'][3])
    
    for i, im in enumerate(data['images']):   
        if i == imageID:
            print(im)
    

def folder_structure(raw_dir, task, dataset):
    sequenceDict = {}
    if task == 'tracking':
        if dataset == 'VisDrone':    
            directoryList = os.listdir(raw_dir)
            datasets=[]
            for dSet in directoryList:
                try:
                    datasets.append(dSet.split('-')[2])
                    annotationDir = raw_dir + '/' + dSet + '/annotations'
                    sequenceDict[dSet] = [ sequence.rstrip('.txt') for sequence in os.listdir(annotationDir)]
                except:
                    print("There is a problem with the VisDrone dataset, please do not change the unzipped folder names!")
            #assert datasets == ['test','train', 'val'], "There is a problem with the VisDrone dataset, please do not change the unzipped folder names and remove the .zip folders!"
            #assert len(datasets) == 3, "Please download trainset (7.53 GB), valset (1.48 GB) and testset-dev (2.145 GB) datasets, excluding testset-challenge (2.70 GB)!"
            return sequenceDict
    

def annotation_processor(raw_dir, data_dir, task, dataset, folderStructure):
    if task == 'tracking' and dataset == 'VisDrone':
        for dSet in folderStructure:
            print("Working on: ", dSet)
            imageDirectory = data_dir + dataset + '/' + dSet + '/images/'
            annotationDirectory =  raw_dir + dSet + '/annotations/'
            newTrainAnnotationDirectory = data_dir + dataset + '/' + dSet + '/labels/'
            imagesArr = sorted(os.listdir(imageDirectory))

            for i, image in enumerate(imagesArr):
                imageDir = imageDirectory + image
                im = Image.open(imageDir,"r")
                width, height = im.size

                fileName = image.split('-')[0] + '.txt'
                sequenceID = int(image.split('-')[1].split('.jpg')[0])
                f = open(annotationDirectory + fileName, "r")
                lines= f.readlines()
                newAnnotationFile = open(newTrainAnnotationDirectory + image.rstrip('.jpg')+ '.txt', 'w+')
                for i, line in enumerate(lines):
                    lineList = line.rstrip('\n').split(',')
                    if int(lineList[0]) == sequenceID:
                        x_top = int(lineList[2])
                        y_top  = int(lineList[3])
                        w = int(lineList[4])
                        h = int(lineList[5])

                        x_center=np.absolute(np.float32(np.abs(x_top+(w/2))/width))
                        y_center=np.absolute(np.float32(np.abs(y_top+(h/2))/height))

                        classID = int(lineList[7])

                        tempLine = str(classID) + '\t' + str(x_center) + '\t' + str(y_center) + '\t' + str(w/width) + '\t' + str(h/height)
                        newAnnotationFile.write(tempLine + '\n')
                newAnnotationFile.close()
        

def image_directory_processor(raw_dir, data_dir, task, dataset, folderStructure):
    if task == 'tracking' and dataset == 'VisDrone':
        for dSet in folderStructure:
            for sequence in sorted(folderStructure[dSet]):
                imageFolder = raw_dir + dSet + '/sequences/' + sequence + '/'
                images = os.listdir(imageFolder)
                for i, image in enumerate(sorted(images)):
                    if i >= 0:                
                        originalImage = cv2.imread(imageFolder + '/'+image, cv2.IMREAD_COLOR)
                        newDirectory = data_dir + dataset + '/' + dSet + '/images/' + sequence + '-' + image 
                        cv2.imwrite(newDirectory, originalImage, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='VisDrone', help='VisDrone, skydata') 
    parser.add_argument('--task', type=str, default='tracking', help='tracking, detection')
    parser.add_argument('--raw-dir', type=str, help='the full directory to the downloaded raw datasets', required=True)
    parser.add_argument('--data-dir', type=str, help='the full directory to dataset to be used by yolov5', required=True)  
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt
    

def main(opt):
    folderStructure = folder_structure(opt.raw_dir, opt.task, opt.dataset)
    image_directory_processor(opt.raw_dir, opt.data_dir, opt.task, opt.dataset, folderStructure)
    annotation_processor(opt.raw_dir, opt.data_dir, opt.task, opt.dataset, folderStructure)
    

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)