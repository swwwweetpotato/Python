# 난수 ramdom number를 생성하는 모듈
# 난수를 통해서 간단한 게임을 제작할 수 있고 확률 처리도 할 수 있다.

import random
# 1. randint() : 두 인수 범위 내에 정수를 임의로 생성

print(random.randint(1, 10))

# 2. randrange() : range()와 사용방법이 비슷,
# range() : 특정 범위 정수값을 모두 생성
# randrange() : 그 특정 범위에 속한 정수중 하나만 임의로 생성
print(random.randrange(10))
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))

# 3. random() : 0이상 1미망 범위에서 임의의 실수를 생성
print(random.random())

# 50% 확률로 '안녕하세요'출력

rand = random.randint(1, 2)
if rand == 1:
    print('안녕하세요')

# 4. choice() : 전달된 시퀀스 자료형에 속한 요소 중에서 하나를 임의로 반환
seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

idx = random.randint(0,3)
print(seasons[idx])

# 5. sample() : 전달된 시퀀스 자료형 요소 중 지정된 개수의 요소를 임의로 반환
# 반환 결과는 list 자료형이며 중복없이 임의의 요소가 선택
print(random.sample(range(1, 101), 10))     # 1-100사이에 랜덤으로 10개 추출


# 6. shuffle()
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
