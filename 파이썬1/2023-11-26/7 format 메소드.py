# format() : 변수나 값을 표시하고, 해당 값이 표시될 위치를 중괄호({})로 표시하는 방식

print('My name is {}'.format('james'))
print('My name is {name}'.format(name='james'))
print('My name is {}. I\'m {}years old'.format('james', 25))
print('My name is {1}. I\'m {0}years old'.format(25, 'james'))

# f-string (formatted strings) : 파이썬 3.6이후 버전에서 사용 가능

who = 'you'
how = 'happy'
print(f'{who} make me {how}')

age = 25
print(f'내년엔 {age+1}살이 됩니다.')