# VIRUS
손을 인식해서 손 세정제를 뿌려주는 시스템

https://github.com/yeechaann/virus


- 시스템 블럭
1) 사람이 접근하여 카메라에 손을 내민다.
2) 서보모터를 동작시켜 소독제를 펌핑한다.
3) 남은 용량을 계산하여 보여준다.
![스마트손소독제](https://user-images.githubusercontent.com/152094/87102900-6262ad00-c28e-11ea-9217-76088e512ddc.png)
  
- 소프트 WBS
1) 카메라를 이용한 손 인식
2) 서보모터 제어
3) 카운터를 이용해서 소독제 용량 남은 용량 알림



## 참고 자료
- 각도 정하는 함수
~~~
def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)
~~~