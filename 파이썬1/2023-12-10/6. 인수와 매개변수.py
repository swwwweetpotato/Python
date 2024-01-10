# 함수로 전달되는 인수(argument)를 저장하는 변수를 매개변수(parameter)라고 한다.

# 1. 인수가 있는 함수

def introduce(name, age):
    print(f'내 이름은 {name}이고, 나이는 {age}살 입니다.')

introduce('bok', 23)
introduce(age=23, name='용복이')

def show(*args):    # * : 매개변수가 몇개 들어올지 모른다!!
    for item in args:
        print(item)


show('python')
show('happy', 'birthday')

# 3. 디폴트 매개변수
# 매개변수로 전달되는 인수가 없는 경우에 기본적으로 사용

def hello(message='안녕하세요'):
    print(message)

hello()
hello('만나서 반갑습니다.')

# 디폴트 매개변수가 있는 경우 뒤로 배치
def hello2(name, message='안녕하세요'):
    print(f'{name}님 {message}')

hello2('복이')
hello2('한이','반갑습니다.')


