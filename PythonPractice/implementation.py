# 구현의 대표적인 문제

# 하루 24시간중에 (3 이라는 숫자)가 시 분 초에 몇번들어갈까?
# 랜덤으로 x시간을 받았을때 3이라는 숫자가 과연 몇번 들어갈까?
# 새어보는 프로그램을 만들려고해.

# 5 = 5시
# 5시 59분 59초
# 한번이라도 3이 들어가면 카운트 1을 해준다.
# 2시 30분 24초 = +1
# 5시 33분 53초 = +1
# 3시 00분 00초 = +1

# 카운트는 몇개인가요? ?개
a = int(input())
count = 0

for h in range(a + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)