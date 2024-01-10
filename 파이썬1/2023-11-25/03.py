#변수

str = 'Hello Python'
print(str)
print()
print(str)

#위의 경우 문자열 변수를 사용하여 메모리에 저장.

#변수명 생성규칙
#1. 영문, 한글, 숫자, 언더바(_)로 구성
#2. 특수문자는 사용이 안된다.
#3. 대소문자는 구분인 된다.
#4. 변수명의 첫 글자는 숫자를 사용할 수 없음
#5. 키워드(list, dict, if, for, and...)등은 사용할 수 없음

#권장하는 변수명
#1. 가급적 영문 소문자로 작성
#2. 한글을 사용하지 않고 영어 병수명 사용
#3. 변수명으로 저장된 데이터 유추가 가능하도록 사용

name = 'Alice'
age = 25
address = '''우편번호 12345
서울시 영등포구 여의어쩌고 
저쩌고'''          # multiple line 문자열 저장

boyfriend = None  # 아무것도 저장하지 않음 (like null)
heigt = '170.5'
print(name)
print(age)
print(address)