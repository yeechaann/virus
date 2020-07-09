# VIRUS
손을 인식해서 손 세정제를 뿌려주는 시스템

https://github.com/yeechaann/virus


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