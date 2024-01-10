# break문
# while문이나 for문과 같은 반복문을 강제로 종료하고자 할 때 사용하는 제어문
# 반복문 내에 break문이 나타나면 break문이 포함된 반복문은 종료

n = 1
while n <= 10:
    print(n)
    n += 1
print(n)

n = 1
while True:
    print(n)
    if n == 10:
        break  # while문이 종료 됨
    n += 1

    # print -> break -> n += 1 이나와야지 10까지 출력


while True:
    city = input('대한민국의 수도는 어디인가요?>>>')
    city = city.strip()  #strip() : 양쪽 공백을 제거
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
        print('정답입니다')
        break
    else:
        print('오답입니다. 다시 시도하세요')