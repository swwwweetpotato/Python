money = 9000

# 나이를 입력받아 19세 이상이면 1250원, 13-18세: 1050원, 7-12세: 650원, 7세 미만: 무료
# 잔액은 ...입니다.

def bus_charge(age):
    if age >= 19:
        charge = money - 1250
    elif age >=13 and age <=18:
        charge = money - 1050
    elif age >= 7 and age <= 12:
        charge = money - 650
    else:
        charge = money
    return (f'잔액은 {charge}입니다.')

print(bus_charge(23))
# 사용자로부터 하나의 정수를 받아 정수가 홀수인지 짝수인지 판별하여 출력
user = int(input('숫자를 입력하세요'))
if user%2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')


# 사용자로부터 정수를 입력받아 해당 정수의 구구단을 출력하는 프로그램을 작성하시요
user = int(input('숫자를 입력하세요'))
for i in range(1, 10):
    print(f'{user} * {i} = {user * i}')

# 사용자로부터 여러 개의 숫자를 입력받아 입력된 숫자 중에서 가장 큰값을 찾아 출력하는 프로그램을 작성
# 숫자는 무한대로 입력받을 수 있으나 -1이 입력되는 순간 종료되며, 큰값을 출력을 하게 됨
li = []

while True:
    user = int(input('숫자를 입력하세요.'))
    if user == -1:
        break
    else:
        li.append(user)

li.sort()
print(li[-1])

# 사용자로부터 하나의 정수를 입력받아 해당 숫자만큼 높이를 가진 삼각형 모양의 별을 출력하는 프로그램을 작성
user = int(input('숫자를 입력하세요'))
i = 0
while i != (user+1):
    print(i*'*')
    i += 1