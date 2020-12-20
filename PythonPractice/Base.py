
for i in range(5):
    print(i)


arr = [4, 2, 1, 4, 5]
for i in arr:
    print(i, end=' ')



# input은 무조건 string개념 연산을 하려면 int나 맞는 것을 넣어줘야 한다.
i = input(int(i))
print(i)


# .는 앞에있는 값에 뒤에있는 함수를 입혀주는 개념
# map(), filter()

arr = input().split(' ')
arr = list(map(int, arr))

print(arr)

# .는 앞에있는 값에 뒤에있는 함수를 입혀주는 개념
# map(), filter()

# arr = input().split(' ')
# arr = list(map(int,arr))

arr = list(map(int, input().split(' ')))

print(arr)

while i > 0:
    print("i는 현재 {0} 입니다.".format(i))
    i = i - 1

for i in range(3):
    for j in range(3):
        print("지금 i 값은 {0} j값은 {1}입니다.".format(i, j))

arr = [1, 2, 3, 4, 5]
arr[3] = 7
arr.append(6)  # 맨 마지막 값에 추가시킨다
arr.pop(1)  # arr pop[1] 1번째 배열에 있는 값을 없앰

print(arr)

arr = [1, 2, 3, 4, 5]
arr[3] = 7
arr.append(6)  # 맨 마지막 값에 추가시킨다
arr.pop(1)  # arr pop[1] 1번째 배열에 있는 값을 없앰

print(arr)

# tuple - 수정이 불가(password, id)
tu = (1, 2, 3, 4, 5)

# dictionary - key값 : 가치(value), key값 : 가치(value)
di = {"김치": "1000원", "무": "1500원", "책": "15000원"}
print(di["김치"])

# sort c언어는 25줄정도

arr = [4, 2, 1, 4, 5, 2, 1]
arr.sort()
arr.reverse()
print(arr)

'''
tab: 띄어쓰기
shift + tab: 띄어쓰기
되돌아가기
ctrl + / = 전체
주석처리
'''

arr = [4, 2, 1, 4, 5, 2, 1]
arr.sort()
print("제일 작은 값은 %d 입니다. " % arr[0])
print("제일 큰값은 %d 입니다." % arr[-1])


i = 3
j = 1

print("현재 i의 값은 %d j 값은 %d입니다." % (i, j))

# 반올림은 자동으로, 반올림을 쓰고싶지 않을 땐

i = 3.1
j = 1.23

print("현재 i의 값은 %0.1f j 값은 %0.2f입니다." %(i,j))

'''
round #(실수,몇째자리 소수)  # 소수점 자리수
import math # 수학함수를 쓸수있음
math.ceil(i) : 올림
math.floor(i) : 내림
math.trunc(i) : 버림
'''

format(42, 'b')
'101010'
format(42, 'o')
'52'     #10 진수 포멧으로 다른진수 프린트
format(42, 'x') # (16진수 hex 8진수 oct 2진수 bin)
'2a'
format(42, 'X')
'2A'


# n값을 받을건데 n 값만큼 프린트를 하고싶다
i = input()
i = int(i)

while True:
    print("이 구문은 {0}번 실행이 되었어요".format(i))
    i = i - 1
    if i < 0:
        break
print("반복문에서 탈출했습니다.")


s = input()

for i in range(1, len(s)):
    print("{0}번 반복했어요".format(i))


i = 321

print("%04d" % i) # % 를 쓰면 뒤에 % 를 또 써줘야함


arr = list(map(int, input().split('.')))
print("%04d" % arr[0], "%02d" % arr[1], "%02d" % arr[2])


arr = list(map(int, input().split('.')))
print("%04d.%02d.%02d" % (arr[0], arr[1], arr[2]))


if i % 2 == 0:
    print("짝수입니다.")
elif i % 2 == 1:
    print("홀수입니다.")

# 틀린 답
i = int(input())
x = 0
y = 0
for i in range(i):
    arr = list(map(int, input().split(' ')))
    if arr[1] / arr[0] > 0:
        x = int(arr[1] / arr[0]) * 2
    if arr[1] % arr[0] > 0:
        y = 1
    if arr[0] > arr[1]:
        y = y + 1
    print(x + y)
    y = 0

# 맞은 답
i = int(input())
x = 0
y = 0
for i in range(i):
    arr = list(map(int, input().split(' ')))
    if arr[1] / arr[0] > 0:
        x = int(arr[1] / arr[0]) * 2
    if arr[1] % arr[0] > 0:
        y = 1
    if arr[0] > arr[1] or (arr[1] % arr[0] > (arr[0] / 2)):
        y = y + 1
    print(x + y)
    y = 0


# 커피숍 문제

arr = list(map(str, input().split(' ')))
j = 0
for i in arr:
    j = j + 1
    print("{0}번 손님은 {1}입니다".format(j, i))

for i in range(1, len(arr) + 1):
    print("{0}번 손님 커피 준비되었습니다.".format(i))


# 스타벅스에서 기다리기가 싫음
# 5번 불렀을 때 손님이 가져가지 않으면 버릴거야 커피를
# xxx 손님 (커피)가 준비되었습니다. 1번
# xxx 손님 (커피)가 준비되었습니다. 2번
# xxx 손님 (커피)가 준비되었습니다. 3번
# xxx 손님 (커피)가 준비되었습니다. 4번
# xxx 손님 (커피)가 준비되었습니다. 5번

# xxx 손님 준비되었던 커피가 버려졌습니다.

# 토르 아메리카노

arr = list(map(str, input().split(' ')))

for i in range(1, 6):
    print("{0}손님 {1}가 준비되었습니다.{2}번".format(arr[0], arr[1], i))

print(arr[0] + "손님 커피가 버려졌습니다.")


# 5번 부르고 옆에 놓고 다음 손님을 불러 5번
# 토르가 왔어 8번째 불렀을 때 옴
# 토르 아메리카노 아이언맨 라떼
# 8
# 보관된 커피가 있으면 뒤에 문구가 출력됨 (토르님의 커피 보관중)

arr = list(map(str, input().split(' ')))
arr2 = int(input())

for i in range(1, 6):
    print("{0}손님 {1}가 준비되었습니다.{2}번".format(arr[0], arr[1], i))
for j in range(1, 6):
    if j < 4:
        print("{0}손님 {1}가 준비되었습니다.{2}번 + (토르님의 커피 보관중)".format(arr[2], arr[3], j))
    elif j > 3:
        print("{0}손님 {1}가 준비되었습니다.{2}번".format(arr[2], arr[3], j))



from random import *

print(randint(1, 10))


from random import *

arr = [1, 2, 3, 4, 5, 6]

shuffle(arr)

print("1등은" + str(arr[0]) + " 입니다.")
print("1등은" + str(arr[1]) + " 입니다.")
print("1등은" + str(arr[2]) + " 입니다.")

# arr = []
# arr.append(0)
# arr.append(1)
# arr.append(5)
# arr.append(2)
#
# print(arr)


# 1. 틀린 답
from random import *

for i in range(1, 7):
    arr = randint(1, 100)
    if (i < 2):
        print("1등은 {0}번 맥북입니다. 축하합니다.".format(arr))
    elif (i < 4):
        print("2등은 {0}번 에어팟set입니다. 축하합니다.".format(arr))
    elif (i < 7):
        print("3등은 {0}번 백화점 상품권3매입니다. 축하합니다.".format(arr))

for i in range(1, 5):
    arr2 = randint(1, 100)
    print("4등은 {0}번 시식권입니다. 축하합니다".format(arr2))

# 2. 맞은 답
from random import *

arr1 = []

same = 0
count = 0
while True:
    x = randint(1, 10)
    if x in arr1:
        continue
    else:
        arr1.append(x)
        count = count + 1

        if count == 6:
            break

for i in range(1, 12):
    if i == 1:
        print("1등은 {0}번 맥북입니다. 축하합니다.".format(arr1[0]))
    elif 1 < i < 4:
        print("2등")
    elif 3 < i < 7:
        print("3등")
    else:
        print("4등")


arr = [[0 for col in range(5)] for low in range(5)]

for i in range(5):
    print(arr[i])


# 전자레인지문제

n = int(input())
a, b, c = 0, 0, 0
if n % 10 != 0:
    print(-1)
else:
    a = n // 300
    b = n % 300 // 60
    c = n % 300 % 60 // 10
    print(a, b, c)

