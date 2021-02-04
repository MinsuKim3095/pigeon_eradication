# pigeon_eradication[비둘기 박멸]
Let's create a device that recognizes pigeons and drives them out.  
  
# 계획
비둘기 인식 -> 비둘기가 싫어한다고 하는 계피향 분출하는 장치 만들기  
  
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
- 180 degree servo motor x 1  
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
- 현재 점퍼선이 아직 오지않아 연결 못하는 중  
- 라즈베리파이4 X USB형 웹캠 연결 확인 
