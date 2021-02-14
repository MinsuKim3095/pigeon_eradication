# pigeon_eradication[비둘기 박멸]
Let's create a device that recognizes pigeons and drives them out.  
  
# 계획
비둘기 인식 -> 비둘기가 싫어한다고 하는 계피향 분출하는 장치 만들기  
-> 데스크탑[비둘기가 학습된 Yolo_v4를 이용한 USB웹캠 실행] + SG90 [180 Degree]를 이용하여 좌우  + 물총도 함께 회전  
-> 웹 웹캠에서 비둘기를 인식 시, 비둘기 Bounding box의 중앙 좌표 값을 계산하여 php 파일로 Raspberry Pi 4로 전송.  
-> Raspberry Pi 4에서 php와 mysql을 이용한 server를 만들고, 중앙 좌표 값을 php 파일로 받기  
-> 동시에 SG90 모터 정지 후,[카메라 및 물총 회전 정지] + 물총 트리거에 설치해놓은 MG996R [360 Degree]를 이용하여 해당 지점에 물총 발사
  
# 참고사이트  
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html  
https://github.com/aleju/imgaug#documentation  
https://junyoung-jamong.github.io/machine/learning/2019/01/23/%EB%B0%94%EC%9A%B4%EB%94%A9%EB%B0%95%EC%8A%A4%EB%A5%BC-%ED%8F%AC%ED%95%A8%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A6%9D%ED%8F%AD%EC%8B%9C%ED%82%A4%EA%B8%B0-with-imgaug.html  
https://lee-yunseok.tistory.com/entry/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC-%ED%8C%8C%EC%9D%B4-4-%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C-%EB%8D%B0%EC%8A%A4%ED%81%AC%ED%86%B1-%EA%B5%AC%EC%84%B1-%EB%B0%8F-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95%EB%B2%95

  
2021/1/20  
labelImg를 통해 Image Labelling 완료

2021/1/22  
Image_Augmentation_Pigeon.ipynb를 사용하여 Image Augmentation 완료  
(XML에 있는 Bounding Box포함)  

2021/1/22  
경로 설정에 한글이 포함되있어서 xml파싱 / Training Data 학습 시 유니코드 에러 발생.  
다 지운 뒤 한글이 없는 경로에서 다시 시도.  
  
2021/1/23
Use `tf.cast` instead.
INFO:tensorflow:Waiting for new checkpoint at models/my_ssd_resnet50_v1_fpn
I0123 01:20:55.086144  1204 checkpoint_utils.py:139] Waiting for new checkpoint at models/my_ssd_resnet50_v1_fpn

학습중인데 멈춰있어서 기다리는 중,(2021/1/23 01:23am)
Tensorflow 2.2.0을 깔면 Use'tf.cast' instead. 에서 Stuck  
Tensorflow 2.4.0을 깔면 위의 메세지에서 Stuck 상태.  
진행상태 계속 확인 중  
  
Timeout Error(03:27am)  
waiting for new checkpoint에서 진행되지 않음  
colab으로 자고 일어나서 다시 진행해볼 예정  
기존 사용 내역 :  
Anaconda 가상환경(Tensorflow 2.4.0 / python 3.6 / cuDNN 10.1 / cuda 7.1 / jupyter notebook / .py 파일은 terminal을 통해 실행)  
  
2021/01/24  
Yolo_v4 구동 완료  
참고 자료  
https://www.youtube.com/watch?v=sUxAVpzZ8hU  
  
# 개발환경 (Software)
- python 3.7.7  
- cuda 10.2  
- cudnn 7.6.5.32 for cuda 10.2  
- openCV 4.1.0  
- opencv_contrib  
- cmake 3.17.2  
- Visual Studio 2019  
- labelImg  
- Yolo_Mark  
  
# 개발환경 (Hardware)  
- Raspberry pi 4 ( Raspbery pi OS 32bit )
- 180 degree servo motor x 2  
- 360 degree servo motor x 1  
- Auto Water Gun

# 학습 결과  
2021/01/27  
- yolo-obj.cfg  
- classes = 1, 마지막 convolutional filters를 30 (Class 갯수)+5)*5로 설정.  
- height와 width는 첫 딥러닝이다보니 가늠이 가지않아 416 x 416으로 낮게 수정.
- subdivisions = 16  
- max_batches = 2000 (Class 갯수 * 2000)  
- steps = 1600,1800 (0.8max_batches / 0.9max_batches)  
- image 190장 (원본 20장 + Augmentation 170장 )  
- 사진, 동영상으로 비둘기 인식률 확인 시도  
- 옆모습과 전체 사진만 있어서 몸만 나오거나 정면을 보고 있을 경우 인식률이 좋지 않음.  
- 비둘기가 여러마리 작게 있는 사진은 인식하지 못함.  
- Dataset을 추가하여 재학습을 해야겠다.  
- 다양한 모습의 비둘기 사진 필요 (사진이 잘려있거나, 정면, 뒷모습 등)  
  
2021/01/28  
- Yolo_mark 로 labeling을 할 경우, txt파일로 저장되서 image_augmentation_pigeon.ipynb 파일이 txt를 못 읽음  
(xml을 파싱하도록 해놔서)  
- iCrawler로 google에서 비둘기 image 추가 확보 (총 231장, 기존 Augmented Image 제외 후 새로 Augmentation 실행)  
- labelimg로 labeling을 해서 재학습.  
avg = loss값, 손실율의 평균  
iou = 알고리즘이 설정한 바운더리박스와 사용자가 설정한 바운더리 박스의 중첩 면적을 측정,  
이를 합집합의 면적으로 나눈 것. 0.5 이상이면 제대로 검출됐다고 판단.  
- darknet19_448.conv.23 사용  
![chart_yolo-obj](https://user-images.githubusercontent.com/68323158/106045770-be0a6000-6124-11eb-9f76-43b5cb05db2b.png)
  
클릭하면 Youtube로 연결됩니다.
[![yolov4_pigeon training test](http://img.youtube.com/vi/AHaGocULVMA/0.jpg)](https://youtu.be/AHaGocULVMA?t=0s)  

2021/02/03  
- Raspberry Pi 4 [서버용] 환경설정 완료  
- 한글입력기 / LAMP(Linux, Apache2, MariaDB, PHP)
- 인식한 비둘기의 Bounding Box의 중앙값을 서버를 통해 송신할 예정.  
- 180 / 360 Degree servo motor 및 USB 웹캠 연결 필요  
  
2021/02/04  
- SG90 (180degree) X 2 + tilt 거치대 제작 완료  
- 라즈베리파이 GPIO 중 PWM을 지원하는 4개의 핀에 설치할 예정  
- 라즈베리파이4 GPIO PIN Assignments  
- https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2711/rpi_DATA_2711_1p0_preliminary.pdf  
- 현재 점퍼선이 아직 오지않아 연결 못하는 중  
  
2021/02/05  
- SG90, MG996R 라즈베리파이 가동 확인.(PWM지원 = GPIO 12,13,18,19번)  
- 12,13은 PWM0, 18,19는 PWM1로 묶여있지만 각각 구동 가능.  
- 동시에 가동하기위해 pi-blaster를 라즈베리파이에 설치 및 테스트 중.  
- 그 외 다른 방법으로 동시에 가동할 수 있는 방법이 있나 탐색 중.  
  
2021/02/06
- 서보모터 3개가 전부 4.8V~ 라서 GPIO에 있는 5V 핀 2개만 사용.(1 x sg90, 1 x mg996r)  
- Yolo_v4 에 있는 image.c 파일을 고쳐도 bbox 중간지점이 표시되지 않는 현상 발생  
- 좌표 생성 및 추출이 가능해지면 pc <-> raspberry pi4 시리얼 통신을 사용할 예정.  
- Yolo_v2를 사용할지, v_4의 image.c를 더 고쳐볼지 검토 필요.
  
2021/02/10  
- 라즈베리파이4 Gadget mode + putty를 이용,라즈베리파이4를 pc에서 컨트롤.  
- 라즈베리파이4 서버 pc에서 접속 확인.  
- 소켓통신을 통해 pc(webcam+yolo)에서 확인한 정보를 라즈베리파이4의 서버에 전송테스트 해볼 예정.   
- 소켓테스트 성공.  
![socket_connection](https://user-images.githubusercontent.com/68323158/107618371-d2a63680-6c94-11eb-9926-98ea335bbd88.jpg)  
  
2021/02/11  
- darknet_video.py에서 draw_detection_box 내용을 수정하면 bbox안에 점을 찍을 수 있음.  
  
2021/02/13  
- SG90 0 to 180 degree, 180 to 0 degree 계속 회전하도록 설정.  
- MG996R 0 to 360 degree, 360 to 0 degree 으로 회전하게 설정하여 물총 트리거 눌렀다가 뗐다가 반복하게 설정.  
- 비둘기 인식률을 높이기위해 라벨링을 다시 하여 재 학습중, batch=64, subdivisions(mini-batch):64, width, height : 416, max_batches = 4000 으로 수정.  
- html 서버를 이용하여 bbox 중간값을 라즈베리파이 서버로 전송할 예정.   
- 카메라가 수직으로 움직이지는 않으니, 화면의 중심좌표값을 정해놓고, bbox를 인식하면 bbox의 center_x값에 가깝게 가도록 코딩을 해야겠다.
  
2021/02/14  
- 비둘기 Custom Training 다시 함.  
- 인식률 매우 상승  
- bbox 중앙의 좌표값을 계산하여 하얀색 원으로 실시간 표시.  
클릭하면 Youtube로 연결됩니다.  
[![yolo_v4_pigeon_training_test](https://img.youtube.com/vi/e0q-Pqr5URo/0.jpg)](https://www.youtube.com/watch?v=e0q-Pqr5URo)

![chart_yolov4-custom](https://user-images.githubusercontent.com/68323158/107860402-87517b00-6e82-11eb-9c37-0e51da5d0672.png)  
- 앞으로의 계획  
- bbox의 중앙값 좌표를 라즈베리파이로 전송하고, 웹캠의 중앙점 x좌표와 bbox의 중앙점 x좌표를 sg90모터를 이용해 최대한 가깝게 근접시킨후, mg996r 모터를 이용해 물총을 발사하게 만들어야함.  
- bbox좌표 <-> 라즈베리파이의 통신방법을 찾아봐야함.  
- bbox 인식시, sg90을 이용하여 모터가 웹캠의 중앙점 x 좌표에 가깝게 가도록 이동시킬 수 있어야함.  
- 그 후, MG996R를 사용하여 물총을 쏘고, bbox가 사라지면 다시 sg90을 회전시켜야함.
  
2021/02/15
- 소켓통신을 해서 라즈베리파이(서버)에 PC에서 생긴 bbox의 x_center 좌표값을 txt에 실시간으로 갱신.  
- txt의 내용이 바뀔때마다 pc에서 raspberry pi로 해당 값 전송 확인.  
