# 1. 기본 구성
# 객체를 만들어내는 클래스는 객체가 가져야 할 값과 기능을 가지고 있어야 한다.
# 값: 변수, 기능: 함수
# 클래스 = 변수 + 함수

# 클래스를 구성하는 함수는 메소드 method라고 하고
# 1) 클래스 메소드  2) 정적 메소드  3) 인스턴스 메소드로 분리

# 인스턴스 변수와 인스턴스 메소드
# 인트턴스 변수란 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수
# 모든 인스턴스 변수는 self 라는 키워드를 앞에 붙여쥼
# 인스턴스 메소드란 인스턴스 변수를 사용하는 메소드
# 인스턴스 메소드는 반드시 첫 번째 매개변수로 self를 추가해야 함.

class Person:  # Person 클래스를 정의
    # 첫 번째 매개변수가 self이므로 인스턴스 메소드
    # 모든 인스턴스는 who_am_i() 메소드를 호출할 수 있다.
    # 매개변수 self에는 메서드를 호출하는 인스턴스 전달
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달
    def who_am_i(self, name, age, tel, adderess):
        # 인스턴스 변수 = 매개변수. 모든 인스턴스 변수는 최초에 값이 대입되는 시점에 알아서 생성
        self.name = name
        self.age = age
        self.tel = tel
        self.address = adderess


boy = Person()  # 인스턴스 boy 생성. 클래스의 생성자 호출
boy.who_am_i('john', 15, '123-123', 'toronto')  # 인스턴스 메서도 호출
print(boy.name)

# 클래스에 없는 속성도 추가가 가능. 다른언어의 객체와는 다른 방식.
boy.email = 'test@test.com'
print(boy.email)