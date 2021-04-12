#딕셔너리
#순서가 없다
# data = {'a':10, 'b':20, 'c':30, 'd':40}
# print(data['b'])
#
# data={'홍길동':20,'이순신':45}
# print(data['홍길동'],"살")

# data={'홍길동':[20,165,5],'이순신':45}
# print(data['홍길동'][1], "km")
#
# data = {'홍길동':{'나이':20,'키':165.5},'이순신':45}
# print(data['홍길동']['키'])

# data={1:['홍길동',20,165.5],2:['이순신',45,170.5]}
# print(data[2][2])

#딕셔너리에 데이터추가
# data ={}
# data['홍길동']=[45,160.8]
# print(data)

#실습)컴퓨터언어를 입력받아 딕셔너리에 저장
#{'backend':'java','js','python','frontend':'html5'
# computer = {}
# a = input("백엔드언어에 떠오르는 언어을 하나 고르시오")
# computer['backend']= a
# b = input("프론트엔드에 떠오르는 언어를 하나 고르시오")
# computer['frontend']= b
# print(computer)

# #영화순위
# movie={1:"고질라",2:"귀멸의칼날",3:"미나리"}
# print(list(movie.values()))
# print(list(movie.keys())[0])

#set
asia = {'한국','중국','일본'}
asia.add('베트남 ')
asia.add('중국')
asia.remove('일본')
asia.update({'한국','홍콩','태국'})
print(asia)



