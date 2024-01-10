# 특정 조건을 만족하는 동안 반복해서 수행해야 하는 코드를 작성할 때 사용

# while 조건식:
#   반복실행문

n = 1
while n <= 10:
    print(n)
    n +=1

print(n)

# while문의 중첩


j = 1
while j < 10:
    print(f'{j}단 시작')
    i = 1   # i 는 다시 1로 만들어 줘야함!!!
    while i< 10:
        print(f'{j}*{i} = {i*j}')
        i +=1
    j +=1



# 1부터 10사이의 모든 정수를 역순으로 출력

n = 10
while n >= 1:
    print(n)
    n -=1


# 100부터 50사이의 짝수를 출력
n = 100
while n >= 50:
    if n%2 ==0:
        print(n)
    n -=1

