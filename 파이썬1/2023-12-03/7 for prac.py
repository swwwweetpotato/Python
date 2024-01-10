# 출력하고자 하는 구구단을 입력받아 구구단을 출력
for i in range(2, 10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
# set : 비시퀀스 자료형이기 때문에 저장된 요소들 사이에 순서가 없음

for item in {'가위', '바위', '보'}:
    print(item)

# 딕셔너리
person = {'name':'에밀리', 'age':20, 'address':'deagu'}
for i in person:
    print(i)  # key 값만 출력

# value값 출력
for key, value in person.items():  # .items 메소드 사용
    print(f'{key}:{value}')

for key in person:
    print(f'{person[key]}')

for key in person:   # get() 함수를 이용해서 해당 key에 해당하는 value를 가져온다.
    print(f'{person.get(key)}')