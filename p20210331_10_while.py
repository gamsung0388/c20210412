# 반복문:While
# 조건이 참일 동안 실행

# while True:
#     print('python')
#     break

#1부터 10까지 합을 출력
#
# a = 0
# while a<10:
#     a += 1
#     print(a)
# #



# 실습)1~10까지 합
# a = 0 # 합계를 누적할 변수
# s = 0 # 증가하는 변수
# while True:
#     s += 1
#     a += s
#     if s == 10: break
# print(a)

#a가 증가하면서 합계를 구하고 그 합계가 2000이 넘으면 종료
# s = 0 #합계
# a = 0 #증가
# while s<2000:
#     a += 1
#     s += a
#
# print(a, s)

#사용자가 입력한 수를 계속 누적하다가 만약 0을 입력하면 누적합계를 출력
# s = 0 #합계
# p = 1 #name 오류 활성화 필수!
# while p != 0:
#     p = int(input("더할 값은?"))
#     s += p
# print(s)





















