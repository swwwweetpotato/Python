# if : 조건문
# if 조건식:
#   조건식 결과가 True 일 때 실행

num = 15
if num > 0:
    print('양수 입니다') # 조건식이 True라서 실행됨

if True:
    print('양수')

# 들여쓰기 identation 규칙
# 1. 공백 space나 탭tab을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관 없음
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 한다. 공백과 탭을 혼용하여 사용 x, 들여쓰기 수준도 동일해야함.
# 5. 주로 사용하는 들여쓰기는 공백 4개, 탭 1개

if num > 0 : print('양수')  # 실행문이 하나면 한 줄 코드도 가능


# 2. if-else문
# if 조건식:
#   조건식 결과가 True일 때 실행
# else:
#   조건식 결과가 False일 때 실행

num = 6
if num <= 0:
    print('양수')
else:
    print('음수')

# 3. if-elif 문
# if 조건식1:
#   조건식1의 True일 때 결과
# elif 조건식2:
#   조건식2의 True일 때 결과
# ....
# else:
#   모두 False일 경우 결과

score = 80

if score >=90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('D')


# 나이를 입력받아 구분하는 프로그램

age = int(input('나이를 입력하세요>>'))

if age >= 20:
    print('성인 입니다.')
elif age >= 17:
    print('고등학생 입니다.')
elif age >= 14:
    print('중학생 입니다.')
elif age >= 8:
    print('초등학생 입니다.')
else:
    print('미취학 아동입니다.')


# 임의의 정수를 입력받아 해당 값이 3의 배수인지 판별하는 프로그램

q = int(input('정수를 입력하세요>>'))

if q%3 == 0:
    print(f'{q}는 3의 배수입니다.')
else:
    print(f'{q}는 3의 배수가 아닙니다.')


