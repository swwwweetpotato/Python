# 0-9사이 정수를 입력
# 받을 수 잇는 기회는 5번
# 5번 받고나면 '모두 입력되었습니다.' -> '입력된 값은 **입니다.'
# 제약: 0-9사이의 정수를 받지만, 같은 정수를 받을 시 하나로 입력


i = 5
li = []

while i > 0:
    q = int(input(f'0-9사이 정수를 입력하세요. 기회는 {i}번 입니다.>>'))
    li.append(q)
    i -= 1
print('모두 입력 되었습니다.')
print(f'입력된 값은 {set(li)}')