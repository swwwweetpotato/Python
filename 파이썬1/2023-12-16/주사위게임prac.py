# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위 숫자를 맞추는 프로그램
import random
dice = random.randint(1 ,6)

while True:
    q = int(input('주사위값은 얼마일까요?>>'))
    if q == dice:
        print('정답입니다.')
        break
    else:
        print('오답입니다. 다시 시도하세요')
        if dice < q:
            print('다운')
        else:
            print('업')