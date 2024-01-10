# 사용자로부터 임의의 정수를 입력받아 모두 리스트에 보관
# 단 사용자가 0을 입력하면 프로그램 종료, 이때 입력받은 0은 리스트에 보관하지 않음

li = []
q = int(input('정수를 입력하세요>>'))

while q != 0:
    li.append(q)
    q = int(input('정수를 입력하세요>>'))

print(li)

list = []
run = True
while(run):
    num = int(input('정수를 입력하세요'))
    if(num ==0):
        run = False
        print('프로그램을 종료합니다.')
    else:
        list.append(num)
    print(list)


