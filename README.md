### <div align="center">YOLODrone + </div>

This repository is developed for presenting the results for YOLODrone+ which has the similar architecture with YOLOv5.



## Abstract:
The performance of object detection algorithms running on images taken from Unmanned Aerial Vehicles (UAVs) remains limited when compared to the object detection algorithms running on ground taken images. Due to its various features, YOLO based models, as a part of one-stage object detectors,  are preferred in many UAV based applications. In this paper, we are proposing novel architectural improvements to the YOLOv5 architecture. Our improvements include: (i) increasing the number of detection layers and (ii) use of transformers in the model. In order to train and test the performance of our proposed model, we used VisDrone and SkyData datasets in our paper. Our test results suggest that our proposed solutions can improve the detection accuracy.

For Citation: [YOLODrone+: Improved YOLO Architecture for Object Detection in UAV Images]()
<!--
### <div align="center">Raw Data Management</div>
 This repository was designed to solve object detection problem. The first step to solve the object tracking problem is object detection.!!! Therefore, we used VisDrone-MOT Dataset and convert the image and annonation directories to object detection format. To sum up the util.py code is capable of converting the MOT directory format to OD format as well as converting the VisDrone annotation format, same format as coco, to work within YOLO format.

For more explanation please refer to: 
[YOLO Annotation Format](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data#11-create-datasetyaml)
## Creating a directory for Raw Data:
First things first, in order to complete the annotation format transformation and work in a clean environment please create a folder named as VisDrone_raw under the main directory with the following command:
```bash
mkdir VisDrone_raw
cd VisDrone_raw
```
-->
## Downloading Dataset:
Please download Task 4: Multi-Object Tracking dataset from the following official VisDrone GitHub [link](https://github.com/VisDrone/VisDrone-Dataset#task-4-multi-object-tracking).

It is faster to use gdown for downloading from Google Drive. 
```bash
gdown "[gdrive download id]"
```
For every set such as trainset, valset, testset download the .zip folders and unzip them under the VisDrone_raw directory. The following shows a sample directory structure of the valset when the valset is downloaded and unzipped:

```bash
VisDrone_raw
   |——————VisDrone2019-MOT-val
   |        └——————annotations  #annotation folder
   |        |        └——————uav0000086_00000_v.txt
   |        |        └——————uav0000117_02622_v.txt
   |        └——————sequences    #sequence folder which stores the images according to scene footage
   |        |        └——————uav0000086_00000_v       #scene name
   |        |        |        └——————0000001.jpg     #the images which are obtained from scene videos
   |        |        |        └——————0000002.jpg
   |        |        |        └——————0000003.jpg
   |        |        └——————uav0000117_02622_v
   |        |        |        └——————0000001.jpg
   |        |        |        └——————0000002.jpg
   |        |        |        └——————0000003.jpg
```

After all three datasets which are trainset (7.53 GB), valset (1.48 GB) and testset-dev (2.145 GB) downloaded and unzipped please remove the downloaded .zip folders.

## Prepare UAV Datasets
<!---The code for converting [VisDrone Dataset](http://aiskyeye.com/) and [SkyDatav1](https://www.skydatachallenge.com/) is available in this repository. As also mentioned in the official repository of the [YOLOv5](https://github.com/ultralytics/yolov5) the YOLO labelling for is different than COCO. utils.py will convert the coco format of the visDrone and skydata to YOLO format. Also, the code for converting the VisDrone-MOT dataset to VisDrone-DT format is available in this repository. -->

Please check that you are in the correct directory for the following instructions to be working. Make sure that after downloading the VisDrone raw dataset under the VisDrone_raw, you move back to the main directory. To check that you are in the main directory use the following command:

```bash
pwd #The output of the command should be like: .../yolodrone_plus
mkdir datasets #This folder will be used by yolov5
mkdir datasets/VisDrone #The processed annotations and images will be moved here.
mkdir datasets/VisDrone/VisDrone2019-MOT-val
mkdir datasets/VisDrone/VisDrone2019-MOT-val/images
mkdir datasets/VisDrone/VisDrone2019-MOT-val/labels
mkdir datasets/VisDrone/VisDrone2019-MOT-train
mkdir datasets/VisDrone/VisDrone2019-MOT-train/images
mkdir datasets/VisDrone/VisDrone2019-MOT-train/labels
mkdir datasets/VisDrone/VisDrone2019-MOT-test
mkdir datasets/VisDrone/VisDrone2019-MOT-test/images
mkdir datasets/VisDrone/VisDrone2019-MOT-test/labels
```

Then run the following script:
```bash
python3 visdrone-utils.py --raw-dir .../yolodrone_plus/VisDrone_raw/ --data-dir .../yolodrone_plus/datasets/
```


After the raw dataset conversion the folder format under the datasets should be as follows for YOLOv5 to be working properly:
```bash
datasets
   └——————VisDrone
   |         └——————VisDrone2019-MOT-train
   |         |        └——————images
   |         |        └——————labels
   |         └——————VisDrone2019-MOT-val
   |         |        └——————images
   |         |        └——————labels
   |         └——————VisDrone2019-MOT-test
   |         |        └——————images
   |         |        └——————labels
```
The .yaml files for the datasets are available under the datasets. Please do not forget to carry the .yaml files to their proper place under /yolov5/data/ after you clone the original yolov5 repository.
## Train the Object Detection Model YOLOv5
The followingng script can be used to train YOLODrone+ model. Please either make sure that you are under the yolov5 folder or reorganize the directories for the argumants accordingly.  
```bash
python train.py --data data/VisDrone.yaml --cfg models/hub/yoloDronePlus.yaml  --weights '' --batch-size 16
```
### <div align="center">Reproduce Our Results</div>

## Pretrained YOLOv5s Models and YOLODrone Models
The .yaml files presented in this paper are added to the models folder. Please do not forget to move the .yaml files to their proper location after yolov5 repository cloned and installed. You can download pretrained weights from: [Pretrained Weights](https://drive.google.com/drive/folders/1XdEF5qvMkpjcPiV_NVPfnHUiye4APxNe?usp=sharing) 

|Dataset  |Model        |size |AP%    |AR%    |AP% 50 |params
|---      |---          |---  |---    |---    |---    |---
|VisDrone |YOLOv5s      |640  |31.1   |25.5   |22.6   |7,235,389
|VisDrone |YOLOv5s-tr   |640  |33.6   |25.3   |22.9   |7,235,645     
|VisDrone |YOLOv5s-5    |640  |37.9   |21.1   |20.4   |144,281,723    
|VisDrone |YOLODrone    |640  |29.9   |19.3   |48.4   |61,959,200  
|VisDrone |YOLODrone+   |640  |41.9   |20.9   |29.0   |154,646,139
|         |             |     |       |       |       |
|SkyData  |YOLOv5s      |640  |52.7   |35.4   |38.1   |7,235,389   
|SkyData  |YOLOv5s-tr   |640  |46.0   |33.4   |33.9   |7,235,645         
|SkyData  |YOLOv5s-5    |640  |43.1   |32.9   |35.3   |144,281,723       
|SkyData  |YOLODrone    |640  |50.9   |30.5   |36.0   |61,959,200      
|SkyData  |YOLODrone+   |640  |56.0   |32.7   |38.2   |154,646,139
   
<!--
## TODOs
- [ ] support more object tracking datasets
- [x] add the pretrained weights to gdrive
- [ ] MOT implementation for DeepSort and StrongSort
- [ ] MOT test implementation for HOTA metrics
- [ ] add fps results
-->

## Acknowledgement
The codes for training YOLOv5 was retrieved from original [YOLOv5 github repository](https://github.com/ultralytics/yolov5) and modified in order to increase the accuracy of the detector for UAV Datasets especially considering the small objects in these datasets. Therefore, please do not forget to refer and cite original [YOLOv5 github repository](https://github.com/ultralytics/yolov5) for more information. 

## References
- YOLOv5 Github Repository: [YOLOv5](https://github.com/ultralytics/yolov5)
- Vision Transformers Paper: [ViT](https://github.com/google-research/vision_transformer)
