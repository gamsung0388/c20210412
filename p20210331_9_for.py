#반복문 : for
#
# data = [1,2,3,4,5]
# for i in data:  # in data = 범위
#     print("python", x)
#
# data = ["아이유", "이지은", "이지금", "이지안", "장만월"]

# for x in data:
#     print(x)
#
# for x in [2]:
#     print(data[x])
# print(data[0])
# print(data[1])
# print(data[2])

# 실습 0-9 출력

#range(start,stop,step) step:건너뜀
# print(list(range(101))) #stop
# print(list(range(10, 20))) #start, stop

# for x in range(10):
#     print(x)

#합계를 구하기
# s= 0 # 합계를 저장할 변수
# for x in range(1,11):
#     s += x
# print(s)#총합
#     print(s)#1,3,6....55
# s = 0 # 합계를 저장할 변수
# for x in range(1,10001):
#     s += x #s = s + x
# print(s)

#실습)사용자에게 숫자를 입력받아 그수까지 더함
# s = int(input("숫자를 입력해주세요"))
# for x in range(0, s+1):
#     s += x
# print(s)

#break
#실습) 1부터 100까지 합이 2000이 넘을 때의 수를 출력
# s = 0
# for x in range(1,101):
#     s += x
#     if s > 2000:
#         break #반복문을 종료할때
# print(x,s)

#실습) 욕이나 비속어 나오면 강퇴
#
# flag = 0
#
# badlang = ["축하", "감사", "어그로", "아름", "착한"]
# black = ['비속어', '욕']
# for x in badlang:
#     print(x)
#     if x in black:
#         print("강퇴")
#         break

# else: #for 문이 정상수행 했다면 (break문을 실행하지 않았을 때)
#     print("바른말사용")

# if flag == 0:
#     print("바른말 사용")

#continue
# data =[3,4,5,8,9,6]
# for x in data:
#     if x%2 == 1: continue
#     print(x)
# s = 0
# score = input("점수는?").split()
# score = map(int, score)
#
# for x in score:
#     s += x
#
#     if s > 300:
#         print('합격')
#         break
# else:
#     print("불합격")
