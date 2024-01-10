def create_student(name, korean, math, english, science):
    return{
        'name': name,
        'korean': korean,
        'math': math,
        'english': english,
        'science': science
    }

# 학생을 처리하는 함수를 선언
def student_get_sum(student):
    return (student['korean'] + student['math'] + student['english'] + student['science'])

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return print(f'{student["name"], student_get_sum(student), student_get_average(student)}')

students = [
    create_student('이용복', 50, 80, 100, 50),
    create_student('황현진', 80, 55, 65, 80),
    create_student('한지성', 95, 35, 98, 98),
    create_student('양정인', 85, 65, 50, 80)
]

# 학생을 한 명씩 반복
print('이름', '총점', '평균', sep ='\t\t\t\t')
for student in students:
    # 점수의 총함과 평균
    student_to_string(student)

