months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for month, day in enumerate(months):
    print(f'{month+1}달에는 {day}까지 잇땨')

month = 1
for item in months:
    print(f'{month}월 = {item}일')
    month += 1

months_eng = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for idx, day in enumerate(months):
    print(f'{months_eng[idx]} = {day}일')


rainbows = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
for idx, rainbow in enumerate(rainbows):
    print(f'무지개의 {idx+1}번째 색은 {rainbow}입니다.')

scores = []

while True:
    score = int(input('점수를 입력하세요>>'))
    if score < 0 :
        break
    else:
        scores.append(score)
print(f'평균 = {sum(scores)/len(scores)}, 최대 = {max(scores)}, 최소 = {min(scores)}')

