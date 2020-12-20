# 5분 이상 걸리는 손님만 받아
# 10명의 손님을 받고
# 5분 손님은 받지 않습니다.
# 7분 손님은 받지 않습니다.
# 10분 손님은 감사합니다.
# 15분 손님 감사합니다.
# 최대 15분이 최대 손님
# 11명일 때 퇴근하겠습니다.

from random import *
count = 0
while True:
    x = randint(1, 16)
    if x < 5:
        print("{0}분 손님은 받지 않습니다.".format(x))
    elif 5 <= x <= 15:
        print("{0}분 손님 감사합니다.".format(x))
        count = count + 1
    elif x > 15:
        print("{0}분 손님 죄송합니다.".format(x))

    if count == 10:
        break

print("퇴근입니다.")


