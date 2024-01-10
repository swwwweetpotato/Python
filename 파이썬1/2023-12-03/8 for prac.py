# 1부터 5 사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램

for i in range(5, 0, -1):
    print(i)

# 1부터 입력한 정수의 모든 합계

q = int(input("정수를 입력하세요"))
sum = 0
for i in range(q+1):
    sum = sum + i

print(sum)

# 사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일이름'을 입력받아 'baskey'리스트에
# 저장하는 프로그램을 구현

q = int(input('몇 개의 과일을 보관할까요?>>>'))
baskey = []

for i in range(1, q+1):
    fruit = input(f'{i}번째 과일을 입력하세요>>')
    baskey.append(fruit)

print(f'입력받은 과일은 {baskey}입니다.')