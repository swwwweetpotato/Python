# 1-45번까지 총 6개가 나온다.
import random
import time

num = random.sample(range(1, 46), 6)

i = 1
while i <= 6:
    print(f'{i}번째 당첨번호는 {num[i-1]}입니다.')
    time.sleep(2)
    i += 1
print(f'이번 당첨번호는 {num}입니다.')

##############################
# 강사 답
jackpot = []

while len(jackpot) < 6:
    num = random.randint(1, 45)
    if num not in jackpot:
        jackpot.append(num)
        print(f'{len(jackpot)}번째 담청번호는 {num}입니다.')
        time.sleep(2)
jackpot.sort()
print(f'이번 담천 번호는 {jackpot}입니다.')