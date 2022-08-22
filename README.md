### <div align="center">YOLODrone + </div>

This repository is developed for presenting the results for YOLODrone+ which has the similar architecture with YOLOv5.

## Abstract:
The performance of object detection algorithms running on images taken from Unmanned Aerial Vehicles (UAVs) remains limited when compared to the object detection algorithms running on ground taken images. Due to its various features, YOLO based models, as a part of one-stage object detectors,  are preferred in many UAV based applications. In this paper, we are proposing novel architectural improvements to the YOLOv5 architecture. Our improvements include: (i) increasing the number of detection layers and (ii) use of transformers in the model. In order to train and test the performance of our proposed model, we used VisDrone and SkyData datasets in our paper. Our test results suggest that our proposed solutions can improve the detection accuracy.

[YOLODrone+: Improved YOLO Architecture for Object Detection in UAV Images]()

### <div align="center">Clone and Install </div>
Please follow the instructions from the original YOLOv5 model about installing the repository!
Clone repo and install requirements:
```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

### <div align="center">Prepare UAV Datasets</div>
The code for converting [VisDrone Dataset](http://aiskyeye.com/) and [SkyDatav1](https://www.skydatachallenge.com/) is available in this repository. As also mentioned in the official repository of the [YOLOv5](https://github.com/ultralytics/yolov5) the YOLO labelling for is different than COCO. coco2visdrone.py will convert the coco format of the skydata which is in COCO format to visdrone format. Also, the code for converting the VisDrone-MOT dataset to VisDrone-DT format is available in this repository. 

The folder format under the datasets should be as follows:
```bash
datasets
   |——————SkyData
   |        └——————train
   |        |        └——————images
   |        |        └——————labels
   |        └——————val
   |        |        └——————images
   |        |        └——————labels
   |        └——————test
   |        |        └——————images
   |        |        └——————labels
   └——————VisDrone
   |         └——————train
   |         |        └——————images
   |         |        └——————labels
   |         └——————val
   |         |        └——————images
   |         |        └——————labels
   |         └——————test
   |         |        └——————images
   |         |        └——————labels
```
The .yaml files for the datasets are available under the datasets. Please do not forget to carry the .yaml files to their proper place under /yolov5/data/ after you clone the original yolov5 repository. 
### <div align="center">Reproduce Our Results</div>

## Pretrained YOLOv5s Models and YOLODrone Models
The .yaml files presented in this paper are added to the models folder. Please do not forget to move the .yaml files to their proper location after yolov5 repository cloned and installed. 

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
   
## TODOs
- [ ] support more datasets
- [ ] add the pretrained weights to gdrive
- [ ] MOT implementation
- [ ] add speed results

<details open>
<summary>References</summary>
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [ViT](https://github.com/google-research/vision_transformer)
</details>
