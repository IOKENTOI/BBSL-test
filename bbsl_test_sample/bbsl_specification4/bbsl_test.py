import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import sys
import math
import argparse
from .. import function as fc

parser = argparse.ArgumentParser()
parser.add_argument('--labels_path', type=str, default='testing/lables/', help='path to ground truth labels')
parser.add_argument('--direction_area_distance', type=int, required=True, nargs=2, help='value of directionAreaDistance')
parser.add_argument('--stopping_distance', type=int, required=True, nargs=2, help='value of stoppingDistance')
opt = parser.parse_args()
print('Config:')
print(opt)

kitti_labels = os.listdir(opt.labels_path)
kitti_labels.sort()

stopping_distance_x=opt.direction_area_distance
stopping_distance_y=opt.stopping_distance

bbsl_countT = 0
bbsl_countF = 0
iou8_countT = 0
iou8_countF = 0
iou6_countT = 0
iou6_countF = 0

for indexi in range(len(kitti_labels)):
  kitti_label_totest_path = opt.labels_path + kitti_labels[indexi]
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
    elif ((stopping_distance_y[0]<=y2 and stopping_distance_y[1]>=y1)and not(stopping_distance_x[0]<=x2 and stopping_distance_x[1]>=x1)):
      ground_truth_case="xsafe_ywarning"
    elif (not(stopping_distance_y[0]<=y2 and stopping_distance_y[1]>=y1)and (stopping_distance_x[0]<=x2 and stopping_distance_x[1]>=x1)):
      ground_truth_case="ysafe_xwarning"
    else:
      ground_truth_case="Not Stop"
    a=[x1,y1,x2,y2]
    detext_iou = 0
    detect_label = open('detectdata/'+str(kitti_labels[indexi]),'r')
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
        if(detext_iou<fc.ioufunc(a,b)):
          detect_y1 = detect_y1_t
          detect_x1 = detect_x1_t
          detect_y2 = detect_y2_t
          detect_x2 = detect_x2_t
          detext_iou = fc.ioufunc(a,b)
    if(detext_iou == 0):
      object_detection_case="仕様外"
    elif((stopping_distance_y[0]<=detect_y2 and stopping_distance_y[1]>=detect_y1)and(stopping_distance_x[0]<=detect_x2 and stopping_distance_x[1]>=detect_x1)):
      object_detection_case="Stop"
    elif ((stopping_distance_y[0]<=detect_y2 and stopping_distance_y[1]>=detect_y1)and not(stopping_distance_x[0]<=detect_x2 and stopping_distance_x[1]>=detect_x1)):
      object_detection_case="xsafe_ywarning"
    elif (not(stopping_distance_y[0]<=detect_y2 and stopping_distance_y[1]>=detect_y1)and (stopping_distance_x[0]<=detect_x2 and stopping_distance_x[1]>=detect_x1)):
      object_detection_case="ysafe_xwarning"
    else:
      object_detection_case="Not Stop"

    if(ground_truth_case==object_detection_case):
      bbsl_test = "T"
      bbsl_countT = bbsl_countT + 1
    else:
      bbsl_test = "F"
      bbsl_countF = bbsl_countF + 1

    if(detext_iou>=0.8):
      iou8_test = "T"
      iou8_countT = iou8_countT + 1
    else:
      iou8_test = "F"
      iou8_countF = iou8_countF + 1

    if(detext_iou>=0.6):
      iou6_test = "T"
      iou6_countT = iou6_countT + 1
    else:
      iou6_test = "F"
      iou6_countF = iou6_countF + 1

    print('labelpath: %s,ground_truth_case: %s,object_detection_case: %s,bbsl_test: %s,IoU0.8_test: %s,IoU0.6_test: %s' % (kitti_label_totest_path,ground_truth_case, object_detection_case,bbsl_test,iou8_test,iou6_test))

print ('IoU0.6_countT: %s,IoU0.6_countF: %s' % (iou6_countT,iou6_countF))
print ('IoU0.8_countT: %s,IoU0.8_countF: %s' % (iou8_countT,iou8_countF))
print ('bbsl_countT: %s,bbsl_countF: %s' % (bbsl_countT,bbsl_countF))
