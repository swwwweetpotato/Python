# 정수를 입력받아서 그 횟수만큼 'Hello'를 출력
# 0이하의 값이 입력되면 '잘못된 입력입니다.'라는 오류 메시지를 출력

# q = int(input('0이상의 정수를 입력하세요>>'))
# i = 1
#
# if q <= 0:
#     print('잘못된 입력입니다')
#     eixt()
# while i <= q:
#     print(f'{i}번째 hello')
#     i += 1

count = int(input('정수를 입력하세요>>'))
if count <= 0:
    print('잘못된 입력입니다')
else:
    n = 1
    while n <= count:
        print(f'{n}번째 hello')
        n += 1