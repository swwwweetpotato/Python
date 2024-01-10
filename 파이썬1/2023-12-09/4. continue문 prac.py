fruits = ['사과', '수박']
count = 3  # 입력 가능한 횟수


# count == 0 일때 종료, 종료가 되고나서 '5개의 과일은 ...입니다'가 출력 되어야 함.
# 동일한 입력이 입력될 경우 '동일한 과일이 있습니다'라고 출력되고 count는 출력되지 않음

while count > 0 :
    fruit = input('어떤 과일을 저장할까요?>>')
    if fruit in fruits:
        print("동일한 과일이 있습니다")
        continue
    fruits.append(fruit)
    count -= 1
    print(f'입력이 {count}번 남았습니다.')

print(f'5개 과일을 {fruits}입니다.')



