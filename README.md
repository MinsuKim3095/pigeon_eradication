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

