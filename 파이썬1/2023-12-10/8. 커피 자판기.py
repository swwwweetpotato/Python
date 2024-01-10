# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 있는 커피의 종류와 가격
# '아메리카노': 1000, '카페라떼': 1500, '카푸치노': 2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부고하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한커피와 잔돈을 반환

def vending_machine(money,pick):
    print(f'{money}원엔 {pick}을 선택했다')
    menu = {'아메리카노':1000, '카페라떼':1500, '카푸치노': 2000}
    if pick not in menu:
        print(f'{pick}은 없는 메뉴 입니다.')
        return money, '없는 메뉴'
    elif menu[pick] > money:
        print(f'{pick}은 {money[pick]}원 입니다.')
        return money, '금액부족'
    else:
        return money - menu[pick], pick

order = input('커피를 선택하세요(아메리카노, 카페라떼, 카푸치노)')
pay = int(input('얼마를 넣을까요?'))

change, coffe = vending_machine(pay, order)
print(f'잔돈: {change}원, 커피{coffe}')

