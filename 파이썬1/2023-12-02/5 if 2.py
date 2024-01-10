# 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력하는 프로그램을 구현하세요
a = int(input('임의의 정수를 입력하세요>>'))
b = int(input('임의의 정수를 입력하세요>>'))
c = int(input('임의의 정수를 입력하세요>>'))

max = a
if b > max:
    max = b
if c > max:
    max = c

print(max)

# 차량 2부제 실시, 짝수 운행 가능

car = input('차량 번호를 입력하세요>>')

if int(car[-1])%2 == 0:
    print(f'차량번호 {car} 오늘 운행가능합니다.')
else:
    print(f'차량번호 {car} 오늘 운행 불가합니다.')