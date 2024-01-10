# 학생 리스트를 선정. 딕셔너리(idx : value)  요소로 가진 리스트

students = [
    {'name' : '연하진', 'korean': 92, 'math' : 98, 'english' : 96, 'science': 98},
    {'name' : '이용복', 'korean': 78, 'math' : 68, 'english' : 100, 'science': 80},
    {'name' : '양정인', 'korean': 98, 'math' : 35, 'english' : 50, 'science': 85},
    {'name' : '황현진', 'korean': 88, 'math' : 55, 'english' : 80, 'science': 65},
    {'name' : '한지성', 'korean': 65, 'math' : 98, 'english' : 100, 'science': 100}
]

# 학생을 한명씩 반복
print('이름', '총점', '평균', sep ='\t\t\t\t')
for student in students:
    # 점수의 총함과 평균
    score_sum = student['korean'] + student['math'] + student['english'] + student['science']
    score_mean = score_sum / 4
    print(student['name'], score_sum, score_mean, sep = '\t\t\t')

