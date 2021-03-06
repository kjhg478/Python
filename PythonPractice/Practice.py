# Python 기초

print("*" * 7)

'''
주석이 여러 문장으로 가능합니다
'''

# 주석입니다.
'''
1. Quiz ) 변수를 이용하여 다음 문장을 출력하시오
변수명 : station
변수값 : 사당, 신도림, 인천공항 순서대로 입력
출력문장 : XX 행 열차가 들어오고 있습니다.
'''
station = ['사당', '신도림', '인천공항']
print(station[1] + "행 열차가 들어오고 있습니다.")

# 연산자
print(2**3) # 2 ^ 3승
print(5%3) # 나머지 값
print(5//3) # 몫

# 간단 수식
print((3>0) and (3<5)) # true
print((3>0) & (3<5)) # true

print((3>0) or (3 > 5)) # true
print((3>0) | (3>5)) # true

print(5>4>3) # true
print(5>4>7) # false

from random import *
number = (int(random() * 45) + 1)
print(number)
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

'''
2. quiz 당신은 최근에 코딩 스터디 모임을 새로 만들었다.
월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인
조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성해라

조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월 별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

출력문 : 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. 
'''
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")
#date는 int형이기 때문에 + 를 이용하려면 str로 변환해줘야 함
print("오프라인 스터디 모임 날짜는 매월", randint(3, 29) , "일로 선정되었습니다.")

