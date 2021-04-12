#모듈
import time
from _datetime import datetime as d

# print("오늘은",time.localtime().tm_year,"년",time.localtime().tm_mon,"월",time.localtime().tm_mday,"일","만우절입니다.")
# print("현시간은",time.localtime().tm_hour,"시",time.localtime().tm_min,"분",time.localtime().tm_sec,"초","로서 오후수업입니다")

# now = d.now()
# print(now)
# print(now.strftime('%Y-%m-%d %H-%M:%S'))

#sleep 함수 : 프로그램 실행속도를 제어
#실습
#1초마다 타이머
# a = 0
# sec = input("타이머시간을 정해주세요") #맞춘 시간
# print("타이머시작")
# for x in range(int(sec)):
#     time.sleep(1)
#     print( x+1,"초")
#
# print('타이머 종료')

# 맞추기 튜토리얼

# import random
# h = 5
# x = random.randint(1,6)
# while True:
#     a = int(input("주사위를 굴렸습니다 맞춰보세요"))
#     if a == x:
#         print("정답입니다. 나온 수는 %d입니다."%x)
#         break
#     elif a != x:
#         print("맞추실때까지 나가실수 없습니다. 하트가 %d개 소모되었습니다."%h)
#         h -= 1
#         print(h)
#     elif h ==0:
#         print("하트를 모두 소모하셨습니다")
#         break
#

#대결
# m = 0
# it = 0
# i = random.randint(1,6)
# for x in range(3):
#     t = input("주사위를 굴렸습니다. 알파고를 이겨보세요")
#     if int(t) > i:
#         print("이겼습니다")
#     elif int(t) < i:
#         print("졌습니다")
#     else:
#         print("비겼습니다.")

#sample()
# random.sample(range(1,45), 7)



#choice()
# print(random.choice(["가위","바위","보"]))
#
# #shuffle():섞는다
# data = [1,2,3,4,5]
# random.shuffle(data)
# print(data)

import turtle
turtle.shape('turtle')
turtle.color('red')
for x in range(4):
    turtle.forward(150)
    turtle.right(2000)

turtle.done()



