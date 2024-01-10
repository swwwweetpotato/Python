# 딕셔너리를 리턴하는 함수를 선언. 반복되는 키 입력을 줄임

def create_student(name, korean, math, english, science):
    return{
        'name':name,
        'korean':korean,
        'math':math,
        'english':english,
        'science':science
    }

# 학생 리시트 선언
students = [
    create_student('이용복', 98, 55, 85, 72),
    create_student('한지성', 100, 50, 68, 98),
    create_student('땨아아', 100, 100, 100, 100)
    ]

print('이름', '총점', '평균', sep ='\t\t\t\t')
for student in students:
    # 점수의 총함과 평균
    score_sum = student['korean'] + student['math'] + student['english'] + student['science']
    score_mean = score_sum / 4
    print(student['name'], score_sum, score_mean, sep = '\t\t\t')

