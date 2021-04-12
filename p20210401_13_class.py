#class : 객체를 만들기 위한 틀
class Car: # 대문자 개발자들의 객체 지향 언약
    #속성: 필드
    name = 'grander'
    color = 'red'
    pw = False
    #기능: 메소드
    def power(self):
        pw = not Car.pw



c1=Car()
print(c1.name)
c1.power()


c2=Car()
#독립적인 객체 Car()
#파이썬,c++,자바 class