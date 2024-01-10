max_value = None

while True:
    num = int(input('숫자를 입력하세요(종료하려면 -1을 입력하세요)'))

    if num == -1:
        print('시스템을 종료합니다.')
        break

    if max_value is None or num > max_value:
        max_value = num

if max_value is not None:
    print(f'입력된 숫자 중에서 가장 큰 값은 {max_value}입니다.')
else:
    print('입력된 숫자가 없습니다.')