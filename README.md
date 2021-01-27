# pigeon_eradication[비둘기 박멸]
Let's create a device that recognizes pigeons and drives them out.  
  
# 계획
비둘기 인식 -> 비둘기가 싫어한다고 하는 계피향 분출하는 장치 만들기  
  
# 참고사이트  
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html  
https://github.com/aleju/imgaug#documentation  
https://junyoung-jamong.github.io/machine/learning/2019/01/23/%EB%B0%94%EC%9A%B4%EB%94%A9%EB%B0%95%EC%8A%A4%EB%A5%BC-%ED%8F%AC%ED%95%A8%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A6%9D%ED%8F%AD%EC%8B%9C%ED%82%A4%EA%B8%B0-with-imgaug.html  

  
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
  
# 개발환경 
- python 3.7.7  
- cuda 10.2  
- cudnn 7.6.5.32 for cuda 10.2  
- openCV 4.1.0  
- opencv_contrib  
- cmake 3.17.2  
- Visual Studio 2019  
  
# 학습 결과  
2021/01/27  
- yolo-obj.cfg  
- classes = 1, 마지막 convolutional filters를 30 (Class 갯수)+5)*5로 설정.  
- height와 width는 첫 딥러닝이다보니 가늠이 가지않아 416 x 416으로 낮게 수정. 메모리는 부족하지 않으니 더 올려도 될 듯  
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
- iCrawler로 google에서 비둘기 image 추가 확보.  
- labelimg로 labeling을 해서 재학습시킬 예정.
