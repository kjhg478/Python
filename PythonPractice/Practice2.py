jumin = "940718-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지

print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) # 0번째 글자가 대문자인지
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))
# find 함수는 내가 원하는 값이 이 문자열에 없으면 -1을 반환

print(python.count("n"))

# 탈출 문자

# \n : 줄바꿈
# \" \" : 문장 내에서 따옴표
print("저는 'jh' 입니다.")
print('저는 "jh" 입니다.')
print("저는 \"jh\" 입니다.")

# \\ : 문장 내에서 \
'''
Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙 1 : http:// 부분은 제외 => naver.com
규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙 3 : 남은 글자 중 처음 세자리 (nav) + 글자 갯수(5), 글자 내 'e' 갯수 + "!"로 구성

예) 생성된 비밀번호 : nav51!
'''
paw = "http://google.com"
paw2 = paw.replace("http://", "")
paw2 = paw2[:paw2.index(".")]
lastpaw = paw2[:3] + str(len(paw2)) + str(paw2.count("e")) + '!'
print("{0} 의 비밀번호는 {1} 입니다. " .format(paw, lastpaw))