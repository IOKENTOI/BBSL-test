# BBSL-testing-tools
BBSL(Bounding Box Specification Language) is a formal language specifying spatial relation between Bounding Boxes within an image.<br>
This repo performs a specification-based test of image recognition using the specifications of an autonomous driving system written in BBSL.<br>
If you want to try this tool right away, please use [this Notebook on Google Colaboratory](https://colab.research.google.com/drive/1gmMV2YdmlElOjn9Ud4lRGZ1QOs3QoRth?usp=sharing).

## Table of Contents
- [BBSL-testing-tools](#bbsl-testing-tools)
  * [Table of Contents](#table-of-contents)
  * [Original repository](#original-repository)
  * [Installation](#installation)
  * [Detect](#detect)
  * [BBSL test](#bbsl-test)
  * [Paper](#paper)
  * [BBSL Projects](#bbsl-projects)
  * [Credit](#credit)


## Original repository
This repo is forked from [packyan](https://github.com/packyan/PyTorch-YOLOv3-kitti) for image recognition trained from Kitti dataset.<br>
The packyan repo is forked from [eriklindernoren](https://github.com/eriklindernoren/PyTorch-YOLOv3).

### YOLOv3: An Incremental Improvement
_Joseph Redmon, Ali Farhadi_ <br>

**Abstract** <br>
We present some updates to YOLO! We made a bunch
of little design changes to make it better. We also trained
this new network that’s pretty swell. It’s a little bigger than
last time but more accurate. It’s still fast though, don’t
worry. At 320 × 320 YOLOv3 runs in 22 ms at 28.2 mAP,
as accurate as SSD but three times faster. When we look
at the old .5 IOU mAP detection metric YOLOv3 is quite
good. It achieves 57.9 AP50 in 51 ms on a Titan X, compared
to 57.5 AP50 in 198 ms by RetinaNet, similar performance
but 3.8× faster. As always, all the code is online at
https://pjreddie.com/yolo/.

[[Paper]](https://pjreddie.com/media/files/papers/YOLOv3.pdf) [[Project Webpage]](https://pjreddie.com/darknet/yolo/) [[Original Implementation]](https://github.com/pjreddie/darknet)

## Installation
    $ git clone https://github.com/IOKENTOI/BBSL-test.git
    $ cd BBSL-test/
    $ sudo pip3 install -r requirements.txt


##### Download pretrained weights

 Please download [pretrained weights file](https://drive.google.com/file/d/1BRJDDCMRXdQdQs6-x-3PmlzcEuT9wxJV/view?usp=sharing), and put it into `weights` folder, the path:
`weights/yolov3-kitti.weights`

##### Download Kitti 

[The KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/eval_object.php)

and you should transfrom kitti lable to coco label, by using [label_transform](label_transform/README.md)

## Detect

run`detect.py` to detect objects, and please put samples into `data/samples`
defult weights files is `weights/kitti.weights`

## BBSL test

run `test.py`

## Paper
### Specification Based Testing of Object Detection for Automated Driving Systems via BBSL
_Kento Tanaka, Toshiaki Aoki, Tatsuji Kawai, Takashi Tomita, Daisuke Kawakami, Nobuo Chida<br>_

**Abstract** <br>
Automated driving systems(ADS) are major trend and the safety of such critical system has become one of the most important research topics. However, ADS are complex systems that involve various elements. Moreover, it is difficult to ensure safety using conventional testing methods due to the diversity of driving environments. Deep Neural Network(DNN) is effective for object detection processing that takes diverse driving environments as input. A method such as Intersection over Union (IoU) that defines a threshold value for the discrepancy between the bounding box of the inference result and the bounding box of the ground-truth-label can be used to test the DNN. However, there is a problem that these tests are difficult to sufficiently test to what extent they meet the specifications of ADS. Therefore, we propose a method for converting formal specifications of ADS written in Bounding Box Specification Language (BBSL) into tests for object detection. BBSL is a language that can mathe matically describe the specification of OEDR (Object and Event Detection and Response), one of the tasks of ADS. Using these specifications, we define specification based testing of object detection for ADS. Then, we evaluate that this test is more safety-conscious for ADS than tests using IoU.

[Kento Tanaka et al. Specification Based Testing of Object Detection for Automated Driving Systems via BBSL. In: ENASE. 2023. p. 250-261.](https://www.scitepress.org/Papers/2023/119974/119974.pdf)

## BBSL Projects

### Affiliation
[Aoki Laboratory, Japan Advanced Institute of Science and Technology, Ishikawa, Japan](https://www.jaist.ac.jp/is/labs/aoki-lab/en/)

### GitHub links
[https://github.com/IOKENTOI/BBSL-test](https://github.com/IOKENTOI/BBSL-test)<br>
[https://github.com/utatatata/bbsl-coq](https://github.com/utatatata/bbsl-coq)

### Papers
田中健人, et al. 自動運転システムにおける画像を対象とした形式仕様記述言語 BBSL の提案. 研究報告ソフトウェア工学 (SE), 2020, 2020.8. p. 1-8.


宇田拓馬, Coq による BBSL の形式化と検証. 北陸先端科学技術大学院大学先端科学技術研究科修士論文(情報科学), 2021.3.

Kento Tanaka et al. A Formal Specification Language Based on Positional Relationship Between Objects in Automated Driving Systems. In: 2022 IEEE 46th Annual Computers, Software, and Applications Conference (COMPSAC). IEEE, 2022. p. 950-955.

Kento Tanaka et al. Specification Based Testing of Object Detection for Automated Driving Systems via BBSL. In: ENASE. 2023. p. 250-261.


## Credit
```
@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}
```
