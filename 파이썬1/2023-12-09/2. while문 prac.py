# break문을 사용하여 사용자로부터 숫자를 입력받고 입력된 숫자가 10보다 크면 반복문이 종료되고,
# 작으면 계속 반복되는 코드를 만드시오


while True:
    q = int(input('숫자를 입력하세요>>'))
    if q >= 10:
        print('STOP')
        break
    else:
        print('다시 숫자를 입력하세요>>')