# 저장하고자 하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장 가능
# 대괄화 ([]) 또는 list() 함수를 이용해서 생성
# 정수, 실수, 문자열을 각 1개씩 저장하고 있는 리스트

li = [100, 3.14, 'hello']
print(li)
print(type(li))

# 문자열과 동일한 방식으로 인덱싱을 지원
# 저장된 요소들마다 고유번호인 인덱스를 부여하여 순서대로 관리

# 슬라이싱
print()
li = [10, 20, 30, 40]
print(li[::2])

li.append(50)
print(li)

# 요소의 추가와 삭제가 가능
# 새로운 요소를 추가할때는 append()와 insert() 메소드(함수)를 사용
scores = [50, 40, 33]
print(scores)
scores.insert(4, 100)

print(scores)

# pop() : 인덱스를 적지 않으면 마지막 요소 삭제

