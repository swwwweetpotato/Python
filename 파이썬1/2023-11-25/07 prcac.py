student = '31025'

# 반 번호로 나누어 출력하는 프로그램 구현
# ex) 3학년 10반 25번

print(f'{student[0]}학년 {student[1:3]}반 {student[-2:]}번')

def class_num(student_num):
    return f'{student_num[0]}학년 {student_num[1:3]}반 {student_num[-2:]}번'

print(class_num(student))

# 전체 차량에서 숫자 네자리만 출력하는 프로그램

def car_num(car):
    return (f'{car}의 차량번호 4자리는 {car[-4:]}입니다.')

print(car_num('서울2가 1234'))
print(car_num('10가 5468'))