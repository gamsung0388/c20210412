#함수
# data = [5,6,7,8]
# print(sum(data))

#사용자함수 sum정의
#매개변수:리스트, 반환값:합계
# def mysum(data):
#     s = 0
#     for x in data:
#         s += x
#     # print(s)
#     return s
#
# data = [5,6,7,8]
# r = (mysum(data))
# print("리턴값:",r)

#max, min 함수
# data = [5, 18, 4 , 6]
# mx=max(data)
# print('가장큰값:', mx)
# mi=min(data)
# print('가장작은값', mi)

#공통모듈
# def mymax(data):
#     mx = data[0]
#     for x in data:
#         if x > mx:
#             mx = x
#     return mx



# data = [5, 18, 4 , 6]
# print("가장큰값은: ",mymax(data))

#min값을 구하는 함수

# def mymin(data):
#     mi = data[0]
#     for x in data:
#         if x < mi:
#             mi = x
#     return mi
#
# data = [5, 18, 4 , 6]
# print("가장 작은 값은:", mymin(data))

#ord() 함수 code 함수
#한글은 유니코드체계
# print(ord('A'), len('B'))
# print(ord('가'), len('나'), '가'.encode(), '나'.encode() )
#
# print(chr(44032))

#함수를 입력하여  덧셈빨셈곱하기나눗셈 함수
#매개변수 : 두수 변환값 : 결과
# def add(a,b):
#     return a+ b
# def min(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def cal(a,b):
#     return a+b,a-b
#
# print('더하기:',add(10,20))
# print('빼기:',min(10,20))
# print('곱하기:',mul(10,20))
# print('나누기:',div(10,20))
# print('계산:',cal(10,20)[0],cal(10,20)[1])

#실습)월급 구하기/
# 연봉 시급 초과근무시간을 매개변수
# 연봉(year)
# 시급(time)
#초과근무시간(plustime)
#월급 = 연봉/12 + time * 초과근무시간

# def month(y,t,pt):
#     return y/12+t*pt
#
# print(month(30000000,8950,6))
#결합도 응집도

# def month_money(year_money,time_money,overtime):
#     return year_money/12 +time_money + overtime
#
# year = int(input('연봉'))
# time = int(input('시급'))
# overtimes = int(input('추가근무'))
# print(month_money(year,time,overtimes))