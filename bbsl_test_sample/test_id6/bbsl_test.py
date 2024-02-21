import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys
import math

kitti_label_path = '/content/drive/MyDrive/KITTI_MOD_fixed/testing/lables/'
kitti_labels = os.listdir(kitti_label_path)
kitti_labels.sort()

stopping_distance_x=[420,821]
stopping_distance_y=[275,375]

countT = 0
countF = 0

for indexi in range(len(kitti_labels)):
  kitti_label_totest_path = kitti_label_path + kitti_labels[indexi]
  kitti_label_totest = open(kitti_label_totest_path,'r')
  label_contents = kitti_label_totest.readlines()

  for line in label_contents:
    data = line.split(' ')
    y1 = float(data[2])
    x1 = float(data[3])
    y2 = float(data[4])
    x2 = float(data[5])
    if(x1>1242):x1=1242
    if(x2>1242):x2=1242

    if((stopping_distance_y[0]<=y2 and stopping_distance_y[1]>=y1)and(stopping_distance_x[0]<=x2 and stopping_distance_x[1]>=x1)):
      ground_truth_case="Stop"
    else:
      ground_truth_case="Not Stop"
    a=[x1,y1,x2,y2]
    detext_iou = 0
    detect_label = open('/content/BBSL-test/detectdata/'+str(indexi)+".txt",'r')
    detect_y1_t = 0
    detect_x1_t = 0
    detect_y2_t = 0
    detect_x2_t = 0
    detect_y1 = 0
    detect_x1 = 0
    detect_y2 = 0
    detect_x2 = 0
    for detect in detect_label:
      detectdata = detect.split(' ')
      detect_target = detectdata[0]
      if(detect_target == "Car" or detect_target == "Van" or detect_target == "Truck"):
        detect_y1_t = float(detectdata[1])
        detect_x1_t = float(detectdata[2])
        detect_y2_t = float(detectdata[3])+detect_y1_t
        detect_x2_t = float(detectdata[4])+detect_x1_t
        b=[detect_x1_t,detect_y1_t,detect_x2_t,detect_y2_t]
        if(detext_iou<ioufunc(a,b)):
          detect_y1 = detect_y1_t
          detect_x1 = detect_x1_t
          detect_y2 = detect_y2_t
          detect_x2 = detect_x2_t
          detext_iou = ioufunc(a,b)
    if(detext_iou == 0):
      object_detection_case="仕様外"
    elif((stopping_distance_y[0]<=detect_y2 and stopping_distance_y[1]>=detect_y1)and(stopping_distance_x[0]<=detect_x2 and stopping_distance_x[1]>=detect_x1)):
      object_detection_case="Stop"
    else:
      object_detection_case="Not Stop"

    if(ground_truth_case==object_detection_case):
      test = "T"
      countT = countT + 1
    else:
      test = "F"
      countF = countF + 1
    print('labelpath: %s,ground_truth_case: %s,object_detection_case: %s,test: %s' % (kitti_label_totest_path,ground_truth_case, object_detection_case,test))
print ('countT: %s,countF: %s' % (countT,countF))
