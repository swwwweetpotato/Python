# 개인정보의 보안 처리를 위하여 주어진 인수의 일부를 *로 바꾸어 반환하는 함수
# 이를 모듈로 저장하는 프로그램

# secure_name() : 김철수 -> 김**
# secure_no() : 991216-1234567 -> 991216-*******
# secure_phone() : 010-1234-56789 -> 010-****-5678

def secure_name():
    q = input('이름을 입력하세요>>')
    name = q[0] + '**'
    return name

def secure_no():
    reg = input('주민번호를 입력하하세요')
    a = reg.split('-')[0]
    b = reg.split('-')[1]
    return (f'{a}-{b[0]}******')

def secure_phone():
    q = input('전화번호를 입력하세오')
    a = q.split('-')[0]
    c = q.split('-')[2]
    return (f'{a}-****-{c}')


##################################################
# 강사 정답들
def secure_name(name):
    return name[0] + '**'

def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone.replace(phone[4:8], '****')

