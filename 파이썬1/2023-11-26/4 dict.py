# 사전처럼 어떤 단어와 그 단어의 의미로 구성
# '키 key'와 '값 value'를 '단어'와 '단어의 의미'처럼 사용
# 인덱스 사용 x, 키를 인덱스처럼 사용
# 키 값을 알면 저장된 값을 확일할 수 있는 구조

d = {'a': 'apple', 'b': 'banana'}
print(type(d))

print(d['a'])

# 키값의 자료형이 문자열(str)이라면 dict()함수를 이용해서 생성 가능
c = dict(a='apple', b='banana', c='candy')
print(type(c))

# 추가: 새로운 키와 값을 조합해서 작성
dic = {'apple': '사과'}
dic['watermelon'] = '멜론'

# 수정
dic['watermelon'] = '수박'
print(dic)

# setdefault() 메소드를 이용한 추가
me = {'name':'james'}
me.setdefault('age', 20)
# 수정
me.update(age=25)  # 존재하지 않은 키값도 가능
me.update(address = 'deagu')
print(me)

#삭제 : pop()
me.pop('address')  # 파라미터테 키 값만 넣으면 가넝
print(me)