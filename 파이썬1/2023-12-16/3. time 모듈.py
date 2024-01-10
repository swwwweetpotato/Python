import datetime
import time

# 1. time() : 1970년 1월 1일 0시 0분 0초부터 경과된 시간(timestamp) 반환
# 소수점 이하는 마이크로 초를 의미
print(time.time())

# 2.ctime() : 인수로 전달된 시간은 timestamp형식에 맞춰 반환
print(time.ctime(time.time()))

# 3.sleep() : 인수로 전달된 초(second)만큼 시스템을 일시 정시
time.sleep(3)

# 4. datetime() : 날짜와 시간 데이터를 처리할 때 사용
# 1) now() 메소드 : 시스템의 현재 날짜와 시간을 반환
present = datetime.datetime.now()
print(present)

# 2) date() 함수 : 특정 날짜를 반환
birthday = datetime.datetime(2023, 12, 16)
print(birthday)