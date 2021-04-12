
#조건문
# a = -10
# if a>0:
#     print('양수')
#     print("더드세요")
# else:
#     print('음수')
#     print("그만드세요")

#실습)회원등급 출력
#a가 90보다 크면 합격 아니면 재도전
# a = 89
# if a > 90:
#     print("%d 점입니다. 합격하셨습니다."%a)
# else:
#     print("%d 점입니다. 불합격하셨습니다. 재도전하십시오"%a)
#
# a= int(input("몇점입니까?"))
# if a >= 90:
#     print("%d 점입니다. 합격하셨습니다."%a)
# else:
#     print("%d 점입니다. 불합격하셨습니다. 재도전하십시오"%a)

#실습) 비밀번호 체크
#비밀번호가 일치하면 문이 열립니다.
#일치하지않으면 다시확인하세요
# p = '1234'
# a = input("비밀번호를 대시오") # 기존 등록된 비밀번호
# if a == p:
#     print("띠리링 문이 열립니다.")
# else:
#     print("띠띠띠! 다시 확인해주시길 바랍니다")

#어떤 수가 짝수이면 짝수. 어떤 수가 홀수이면 홀수.
# n = int(input("수를 쓰시오"))
# if n == 0:
#     print("홀짝이아닌수")
# elif n%2 == 0 :
#     print("홀")
# else:
#     print("짝")

#실습)100~90점이상 A 89~80 B 79~70 C 69~60 D 59~ F
# score = int(input("점수를 쓰시오"))
# if score >= 90:
#     print("A학점")
# elif score <90 and score>=80:
#     print("B학점")
# elif score <80 and score>=70:
#     print("C학점")
# elif score <70 and score>=60:
#     print("D학점")
# else:
#     print("F학점")

#실습)몸무게와 키를 입력받아서 비만도 테스트
# t = 75
# h = 175
#
# b = (h-100)*0.9
# print("적정체중", b)
# if b*1.05 > float(t) :
#     print("당신은 말랐습니다.")
# elif b*0.95 >= float(t):
#     print("당신은 적정체중입니다.")
# else:
#     print(" 당신은 비만.")

#실습)계산기

# 30 + 20 = 50
# x = input("두수와 기호를 입력해주세요").split()
# print(x)
# # data = input('계산식은?')
# # print(data.split())
# a = int(x[0])
# b = int(x[2])
# sign = x[1]
#
# if sign == '+' :
#     print("%d + %d = %d"%(a,b,a+b))
# elif sign == "-" :
#     print("%d - %d = %d"%(a,b,a-b))
# elif sign == "*" :
#     print("%d * %d = %d"%(a,b,a*b))
# elif sign == "/" :
#     print("%d / %d = %d"%(a,b, a/b))
# else:
#     print("잘못된 기호입니다.")

# 3)
# import os
# print(os.listdir()) #보안에 취약 (eval)
#
# data = input('계산식은?')
# print(eval(data))

#실습) 두수를 입력을 받아서 큰 수를 화면에 띄운다.
# num = input("두수를 입력해주세요").split()
# a = int(num[0])
# b = int(num[1])
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("같습니다 다시 입력해주세요!")
#
#실습)거스름돈 계산 300원 부족 거스름돈 700 계산완료
# goods = int(input("삐빅"))
# cash = int(input("네 %d입니다!"%goods))
#
# if cash > goods:
#     print("거스름돈은 %d 원 입니다."%(cash-goods))
# elif cash < goods:
#     print("%d 원이 부족합니다."%(goods-cash))
# else:
#     print("감사합니다 계산완료되었습니다")

#논리연산자
# a = 10; b = -20
# print(a>0 and b>0)
# print(a<0 and b>0)
# print(a>b)
# print (b>0 or a<0)
# print(not (a>b))
# a = int(input("첫번째 숫자를 입력하세요"))
# b = int(input("두번째 숫자를 입력하세요"))
#
# if a>0 and b>0:
#     print('둘다 양수')
# elif a<0 and b<0:
#     print("둘다 음수")
# elif a == 0 or b == 0:
#     print("0만 아니면 돼")
# else:
#     print("둘중하나가 음수")

# 음식 프로그램 작성 # () = 줄변경가능
food = ({1 : ['자장면', 5500, '중식'], 2 :['짬뽕', 6000, '중식'], 3 :['곰탕', 10500, '한식'],
         4 :['순대국', 6000, '한식'], 5 :['크림파스타',8000, '양식'], 6 :['토마토파스타', 7500, '양식']})

print('-' * 22)
print('롯데 푸드코트')
print('-' * 22)
print('1.자장면\n2.짬뽕\n3.곰탕\n4.순대국\n5.크림파스타\n6.토마토파스타\n')
print('-' * 22)

choice = int(input("메뉴를 선택해주세요 : "))

num = food[choice] #키를 답하는 문장
name = num[0]
pay = num[1]
coner = num[2]
key = food.keys()

if choice in key: #키에서 답하는 문장
    print(name , "을 드시겠습니까?")
    print(pay, "원 입니다.")
    print(coner, "코너입니다.")
else:
    print("다시입력해주세요")


# if문

# if name == "자장면" or name == "짬뽕":
#     print(" %s을 드시겠습니까? %s입니다 "%(name, pay))
# elif name == "곰탕 " or name == "순대국":
#     print(" %s을 드시겠습니까 %s입니다 "%(name, pay))
# elif name == "크림파스타" or name == "토마토파스타":
#     print(" %s을 드시겠습니까 %s입니다 "%(name, pay))
# else:
#     print("잘못누르셨습니다.")

#교수님이 한 if문

# no = input('메뉴는?')
# if no in ['1','2']:  ##print 문에서 가져온 번호
#     print('중식코너')
# elif no in ['3','4']:
#     print('한식코너')
# elif no in ['5', '6']:
#     print('양식코너')
# else:
#     print('다시입력')













