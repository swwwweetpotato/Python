# 온도계 : 섭씨를 화씨 or 화씨를 섭씨를 바꾸시오

from simple_temperature_converter import *

celsius = 25.0
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'{celsius} 섭씨는  {fahrenheit} 입니다.')

fahrenheit = 77.0
celsius = fahrenheit_to_celsius(fahrenheit)
print(f'{fahrenheit} 화씨는 {celsius} 섭씨 입니다.')