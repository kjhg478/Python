'''
QUIZ)
파이썬 코딩 대회
참석률 높이기 위해 댓글 이벤트
댓글 작성자들 중에 추첨 1명 치킨 3명은 커피 쿠폰
추첨 프로그램

조건 1 : 편의상 댓글은 20명 작성 아이디는 1 ~ 20이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위 추천에 중복 불가
조건 3 : random 모듈의 shuffle과 sample 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2,3,4]
-- 축하합니다 --

(활용예제)
'''
from random import *
lst = range(1, 21) # 1부터 20까지 숫자를 생성
lst = list(lst)
print(lst)
shuffle(lst)
winners = sample(lst, 4) # 4명중에 1명 치킨, 3명 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")


# key : value
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet[5]) 
# get은 none이라고 나오지만 get을 쓰지 않고 없는 값을 추출하면 프로그램이 바로 종료 됨

print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)
print(5 in cabinet)

# 새 손님
cabinet[3] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)

# key들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 튜플 : 값 변경이나 추가가 안되지만 속도가 리스트보다 빠름

menu = ("돈까스", "치즈까스") # 값을 안바꿀 때
print(menu)

name, age, hobby = "김종훈", 20, "코딩"
print(name, age, hobby)

# 집합 : 중복이 안되며 순서가 없음
my_set = {1,2,3,3,3}
print(my_set)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))