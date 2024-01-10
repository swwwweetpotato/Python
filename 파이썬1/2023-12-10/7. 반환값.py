# 함수 호출 결과를 반환(return value)
# 반환값이 있으면 함수 내부에서 return문을 통해 값을 변환할 수 있고,
# 반환값이 없으면 함수 내부에 return 문을 작성할 필요가 없다.

def address():
    str = '우편번호1234\n'
    str += '서울시 영등포구 여의도동'
    return str

print(address())

# print(print())  None 반환

# 3. 함수의 종료를 위한 return
# 반환값이 잇으면 return문을 사용해 반환, 반환값이 없으면 return문을 생랼
# 반환값이 없을 때도 return문을 사용하는 경우 -> 함수를 종료시킬 때

def charge(energy):
    if energy <0:
        print('0보다 작은 에너지는 충전할 수 없습니다')
        return   # charge()함수의 종료 의미
    print('에너지가 충정되었습니다.')

charge(1)
charge(-1)

def print_charge(fun):
    fun(0)

print_charge(charge)  # 함수를 함수 호출 시 인수로 사용이 가능


# 함수안에 함수 선언도 가능
def print_greet(name):
    def get_greet():
        return '안녕하세요'
    print(name+'님'+get_greet())

print_greet('김철수')