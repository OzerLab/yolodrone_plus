import os
import shutil
import numpy as np
import json
import cv2

from os import listdir
from os.path import isfile, join

"""
A playground method to see the details of the annotation for object detection task.
It is possible to obtain more information from the .json file according to coco format.
However, since the computer vision challenge we are dealing with is Object Detection then the only the information required 
for the object detection task such as class id and coordinates of bounding box, only those are to be displayed in this method. 
get_annotation_sample('0027_Z_coco.json')
"""
def get_annotation_sample(annotationFileName):
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


"""
Rename the images and save as jpg
"""
def image_directory_processor(imageFolders):
    dirs = os.listdir( imageFolders )
    for dir in dirs:
        images = os.listdir(imageFolders+ dir)
        for i, image in enumerate(images):
            if i == 0:
                originalImage = cv2.imread(imageFolders+dir+'/'+image, cv2.IMREAD_COLOR)
                newName = imageFolders+dir+'_'+image.rstrip('.png')+'.jpg'
                cv2.imwrite(newName, originalImage, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

imageFolders = "/cta/users/oyku/Object_Tracking/dataset/visdrone2021/test/images/"
image_directory_processor(imageFolders)
"""
Create a image dictionary to create the annotation files
"""
"""
f = open("0003_W_coco.json")
data = json.load(f)
print(len(data['annotations']))
for i, ann in enumerate(data['annotations']):
    if i <= 10:
        print(ann['image_id'], ann['category_id'], ann['bbox'][0], ann['bbox'][1], ann['bbox'][2], ann['bbox'][3])
imageAnnotation={
    "0003_W":{},
    "0009_W_0_2000":{},
    "0009_W_2000_4000":{},
    "0010_W_0_2500":{},
    "0010_W_4001_4500":{},
    "0018_W_0000_1000":{},
    "0018_W_1000_2000":{},
    "0018_W_2000_3000":{},
    "0027_Z":{},
}
    "0003_W":{},
    "0009_W_0_2000":{},
    "0009_W_2000_4000":{},
    "0010_W_0_2500":{},
    "0018_W_0000_1000":{},
    "0018_W_1000_2000":{},
    "0027_Z":{},
    0009_W_2000_4000  0010_W_4001_4500  0018_W_2000_3000  0027_Z
"""

imageAnnotation={
    "0027_Z":{},
}

"""
for scene in imageAnnotation.keys():
    annotationDirectory = scene + '_coco.json'
    f = open(annotationDirectory)
    data = json.load(f)
    for i, im in enumerate(data['images']):
        if i == 0:
            imageAnnotation[scene]['height']=im['height']
            imageAnnotation[scene]['width']=im['width']
        imageAnnotation[scene][im['id']]=im['file_name'].replace('/','_').replace('.png','.jpg')
                 

path = "/cta/users/oyku/Object_Tracking/github/Yolov5_DeepSort_Pytorch/datasets/SkyData/skydata-test/images/"
dir_list = os.listdir(path)

actualAnnotationPath = "/cta/users/oyku/Object_Tracking/dataset/skydatav1/test/annotations/"
for scene in imageAnnotation.keys():
    annotationDirectory = scene + '_coco.json'
    for i, ann in enumerate(data['annotations']):   
        try:
            HEIGHT= imageAnnotation[scene]['height']
            WIDTH = imageAnnotation[scene]['width']
                    
            if imageAnnotation[scene][ann['image_id']] in dir_list:
                txtFileName= imageAnnotation[scene][ann['image_id']].replace('.jpg','.txt')
                newAnnfile = open(actualAnnotationPath+txtFileName, "a") 

                x_top = int(ann['bbox'][0])
                y_top  = int(ann['bbox'][1])
                w = int(ann['bbox'][2])
                h = int(ann['bbox'][3])

                x_center=np.absolute(np.float32(np.abs(x_top+(w/2))/WIDTH))
                y_center=np.absolute(np.float32(np.abs(y_top+(h/2))/WIDTH))

                lineToAdd = str(ann['category_id'])+'\t'+ str(x_center)+'\t'+ str(y_center)+'\t'+ str(w/WIDTH)+'\t'+ str(h/HEIGHT)+'\n'
                
                newAnnfile.write(lineToAdd)
                newAnnfile.close()
        except:
            print(scene,ann['image_id'])
            pass
"""
"""
Move some images and annotations to val
"""
"""
valImagePath = "/cta/users/oyku/Object_Tracking/dataset/skydatav1/val/images/"
valAnnPath = "/cta/users/oyku/Object_Tracking/dataset/skydatav1/val/annotations/"
imagePath = "/cta/users/oyku/Object_Tracking/dataset/skydatav1/train/images/"
annPath = "/cta/users/oyku/Object_Tracking/dataset/skydatav1/train/annotations/"
images = os.listdir(imagePath)

for i, ima in enumerate(sorted(images)):
    if i == 0:
        sceneNameTemp = '0003'
    im = ima.split('frame')
    sceneName = im[0].split('_')
    frameName = im[1].split('.jpg')[0].lstrip('_0')
    if sceneNameTemp==sceneName:
        if int(frameName)%12==0:
            valAnnName = valAnnPath + ima.rstrip('.jpg')+'.txt'
            annName = annPath + ima.rstrip('.jpg')+'.txt'
            shutil.move(imagePath+ima,valImagePath + ima)
            shutil.move(annName, valAnnName)
    else:
        sceneNameTemp=sceneName
"""