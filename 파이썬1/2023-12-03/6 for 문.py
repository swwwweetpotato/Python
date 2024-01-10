# 값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문
# 1. 특정 횟수 반복
# 2. 데이테 순회

# for 변수 in 반복가능한 객체:
#   반복 실행문

for i in range(10):
    print(i)

# 반복가능한 객체
# 1. 시퀀스 sequence 자료형 : 순서를 가지고 있는 자료형 (자료형, 리스트, 튜플, range)
# 2. 비시퀀스 non-sequence 자료형 : 순서를 가지고 있지 않은 자료형 (세트, 딕셔너리)
# 3. 문자열도 가능
for ch in 'hello':
    print(ch)

for item in ['가위', '바위', '보']:
    print(item)

# 리스트 내포
# 리스트 생성 시 for문을 유용하게 사용
li = [n*2 for n in [1, 2, 3]]
print(li)

# 조건에 맞는 데이터만 추출
# 리스트 = [표현식 for 변수 in 반복가능한객체 if 조건식]
li = [n*2 for n in [1,2,3,4,5] if n%3 ==1]
print(li)

# 4. range()함수 : range(초기 값, 종료 값, 증감 값)
#   -초기 값 생략 시 0부터 시작
#   -종료 값 생략 불가(종료 값 제외)
#   -증감 값 생략 시 1씩 증가

# range(