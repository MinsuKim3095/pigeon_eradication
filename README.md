# pigeon_eradication[비둘기 박멸]
Let's create a device that recognizes pigeons and drives them out.  
  
# 계획
![구조](https://user-images.githubusercontent.com/68323158/109514419-5d868e00-7ae9-11eb-9b08-bbb70c186a8f.jpg)


# 참고사이트  
[Yolo_v4 Github]  
https://github.com/AlexeyAB/darknet  
  
[Yolo_v4 Tutorial]  
https://www.youtube.com/watch?v=5pYh1rFnNZs  
  
[Darknet_force_gpu error]의 경우, darknet folder를 아래의 폴더로 바꾸기
https://www.dropbox.com/s/5up5i84l60qr778/darknet.zip?dl=0
   
# 개발환경 (Software)
- python 3.7.7  
- cuda 10.2  
- cudnn 7.6.5.32 for cuda 10.2  
- openCV 4.1.0  
- opencv_contrib  
- cmake 3.17.2  
- Visual Studio 2019    
- Yolo_Mark  
  
# 개발환경 (Hardware)  
- Ryzen 3600x Matisse  
- Geforce 1660 Super
- Raspberry pi 4 ( Raspbian )
- 180 degree servo motor x 2  
- 360 degree servo motor x 1  
- Auto Water Gun  
  
  
# 개발환경 (Library)  
- time  (Servo Motor Control)
- pigpiod (Servo Motor Control)  
- socket (Socket Connection)  
- cv2 (Yolo_v4)  
- darknet (Yolo_v4)  
- numpy (Yolo_v4)  
- os  (Yolo_v4)
- math  (Yolo_v4)
- random  (Yolo_v4)
  
# 학습 진행 
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
  
  
2021/02/17  
- 통신 계획 수정  
- Darknet_video.py 에서 bbox center coordinates값을 계속 coordinates.txt에 갱신  
- desktop(client).py [pc] 와 python_socket_server.py [raspberry pi4]를 이용하여 소켓통신으로 실시간 bbox center coordinates값 전송  
- 전송 확인 완료  
  
2021/02/20  
- bbox center coordinates가 아닌, 웹캠의 중심 x값 - bbox의 중심x값을 보내기로 바꿈.  
- 전송 확인 완료.  
- 문제는 bbox가 생기지 않았을때, None 상태일때 어떻게 처리할것인가? 하는 문제.  
- 라즈베리파이에서도 txt파일이 None일때, 계속 감시상태 (0 to 180, 180 to 0)  
- 하지만 값이 생겼을때 str로 들어오기때문에 int로 바꿔주기 위해 int를 걸면 기존에 null값을 인식해서 int로 바꿀수없다는 에러가 뜸  
- 해결책 필요
  
2021/02/21  
- 수정 완료  
- SG90에 웹캠을 설치했지만, 떨림이 너무 심해서 pigpio를 이용해서 재작업  
  
2021/02/22  
- while문으로 모터를 0 to 180, 180 to 0으로 왕복하다가, 객체를 인식하고 추적하는 과정을 거친후, 왕복하게끔 코드 작성 중  
- coordinates.txt 파일을 w+ 모드로 날리고 다시 쓰고 하다보니 실시간으로 읽는 도중에 Null값 / 좌표값 전송이 반복되는 현상 발견  
- r+모드로 하게 될 경우, 좌표가 3자리 -> 1 or 2자리로 바뀌는 경우 맨 마지막 숫자가 남아서 에러 발생  
- r 모드로 다시 테스트 예정  
- yolo가 비둘기뿐만 아니라 다른 사물도 자꾸 인식해서 사진을 다시 새로구해서 라벨링 후 재작업중  
- height와 width를 416,416 -> 512,512로 증가시킴  
- 기존 비둘기가 대량으로 있던 사진 삭제, 비둘기 한마리가 정확하게 나온 사진 위주로 데이터 재구성  
- 라벨링도 최대한 겹치지 않게끔 재조정   

2021/02/23  
- darknet_video.py 에서 webcam x 중앙 좌표 - bbox x 중앙 좌표 값 전송 ok  
- bbox가 없을 경우, 'nothing' 이라고 데이터 전송 ok  
- 소켓통신을 통해 pc -> 라즈베리파이4 데이터 전송 ok  
- 라즈베리파이에서 데이터를 읽고 'nothing' 일 경우, 0 to 180, 180 to 0 degree로 감시 모드 ok  
- bbox가 생겼을 경우(객체 인식 시), bbox를 웹캠의 중앙에 위치하도록 모터 코드 작성 ok  
- bbox가 웹캠의 중앙(오차범위 +-30)에 위치했을 경우, 12번 서보모터 회전 ok  
- bbox가 있었다가 사라질 경우, 다시 0 degree부터 감시모드 시작 ok  
- 문제는.. yolo의 인식이 너무 빨라서 (frame 당 계산) 순간이라도 bbox가 생성되지 않으면 'nothing' 전송  
- 객체를 추적하다가 다시 감시모드로 갔다가를 반복  
- yolo의 인식률을 더 upgrade 하던가,  
- 모터가 회전할때 흔들림을 줄여서 카메라 초점이 엇나가지않게 하던가,  
- 데이터 전송 속도를 줄여서 or yolo 계산 속도를 낮추던가  
- 위 방법들을 수행해봐야 함.
  
2021/02/24  
- 재학습완료, 여러영상으로 테스트 중  

2021/02/25
- 모든 code 작성 완료  
- 물총과 카메라를 연결할 거치대를 구해서 설치하면 OK  
  
2021/02/27  
- 월요일에 나무공방에 모터 + 물총 거치대 제작 의뢰예정  
  
2021/03/01
- 제작 공방을 찾는 중
