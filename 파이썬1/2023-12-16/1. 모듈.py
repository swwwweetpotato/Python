# 모듈이란
# 파이썬 파일(.py)
# 언제든지 사용할 수 있도록 변수나 함수 또는 클래스를 모아 놓은 파일

# 모듈 생성
# converter.py 생성

# 모듈 사용
# 반드시 같은 디렉토리(폴더)에 있어야 한다.
# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때

import converter

miles = converter.killometer_to_miles(150)
print(miles)

# 2. 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법

# ex) from 모듈 import 함수
# ex) from 모듈 import 함수1, 함수2
# ex) from 모듈 import *

from converter import killometer_to_miles

miles = killometer_to_miles(200)
print(f'200km = {miles} miles')

from converter import *
pounds = gram_to_pounds(1000)
print(pounds)

# 4. 별명 사용하기
# 모듈이나 함수를 import하는 경우에 원래 이름대신 alias 지정
# as 키워드 사용

import converter as cvt

miles = cvt.killometer_to_miles(150)
print(round(miles, 2))

from converter import killometer_to_miles as k_to_m

miles = k_to_m(300)
print(round(miles))

from my_secure import secure_name

print(secure_name())
from my_secure import *

print(secure_no())