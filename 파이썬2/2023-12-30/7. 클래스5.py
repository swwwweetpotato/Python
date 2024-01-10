class MyClass:
    # self : 특별한 예약어. 클래스의 인스턴스 메서드 안에서 사용.
    # 해당 메서드가 호출된 인스턴스를 가르킴
    # 생성자(__init__) : 클래스가 만들어질때 무조건적으로 실행되는 함수
    def __init__(self, value):
        # self == MyClass를 가르킴
        self.value = value
        # MyClass의 값

    def print_value(self):
        print(self.value)

obj = MyClass(42)



# 클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        # 매개변수 => cpu에 이정도 메모리 할당해 달라고 선언
        # self => java == this (자기 자신을 가리키는 키워드)
        self.name = name   # 인스턴스 변수
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science   # 메서드

    def get_average(self):
        return self.get_sum()/4

    def to_string(self):
        return f'{self.name}\t, {self.get_sum()}\t, {self.get_average()}'



students = [
    Student('이용복', 50, 80, 100, 50),
    Student('황현진', 80, 55, 65, 80),
    Student('한지성', 95, 35, 98, 98),
    Student('양정인', 85, 65, 50, 80)
]

print('이름', '     총점', '   평균', sep='\t')
for student in students:
    print(student.to_string())