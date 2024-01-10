name = 'KoreaIT'
print('나의 학원은 %s입니다'%name)


# %s == string
print('나의 학원은', name, '입니다', sep='')

print('나의 이름은'+name+'입니다.')

height = 120.5
print('내 키는 %fcm 입니다.'%height)
# %f == floating

weight = 23.5
print('내 몸무게는 %.1fkg입니다.'%weight)

year, month, day = 2023, 11, 26
print('오늘은 %d년 %d월 %d일 입니다.'%(year, month, day))
# %d == decimal(십진법), int


