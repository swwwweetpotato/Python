# 다음은 리스트에 포함된 잘못된 데이터를 모두 제거하는 프로그램
# 리스트에 저장된 정상 데이터는 모두 'a'를 포함한 문자열이며, 그렇지 않은 경우 잘못된 데이터다.

a_list = ['above', 'cookie', 'app', 'about', 'bisket', 'apple', 'april', 'banana']

for i, item in enumerate(a_list):
    if item.find('a') == -1:  # find() : 찾는 문자열이 없는경우 => -1반환
        print(f'{a_list.pop(i)}저게 됩니다.')
        # pop(i) : 인덱스를 지정한 경우 해당 인덱스 요소를 반환하면서 삭제

# 우리나라 전화번호는 '지역번호 - 국번 - 가입자 개별번호' 형식으로 되어있음.
# 어떤 형식의 전화번호를 입력하더라도 '국번'을 추출하여 출력하는 프로그램을 구현하세요

while True:
    q = input('전화번호를 입력하세요>>')
    tele = q.split('-')[1]
    print(tele)

