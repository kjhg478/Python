# 010 1234 5678
# a = "10"
# b = 1234
# c = "5678"
# d = "-"
# print("0"+a+d+str(b)+d+c)
# print("0{0}-{1}-{2}".format(a,b,c))
# print("내 이름은 ",end="종훈입니다."+"\n")
# name, age, language
# name,age,language = input().split()
# print("나의 이름은 {0}이고 나이는 {1}세 이며, 자신있는 프로그래밍 언어는 {2} 입니다.".format(name, age, language))

# list (배열)
# dic ()
# tuple 배열(내맘대로 수정가능, 내맘대로 수정못해)

# arr = [10]
# arr.append(1)
# arr.append(2)
# arr.append(3)
# print(arr)
# arr.pop(2)
# print(arr)

# for(i : arr){
# sysout(i)
# }
# for(int i = 0 ; i < arr.length; i++){
# }

# for i in arr:
#     print("i값은 : "+str(i))
#     for j in range(1,10):
#         print("j값은 : " + str(j))

# 오늘의 번호표 구하는 프로그램
# 스타벅스
# 오늘 갓 내린 브리질산 아라비카 커피를 손님들에게 제공하기위해 
# 스타벅스는 번호표를 뽑기로 하였다.
# 처음오는 손님부터 "1번손님 반갑습니다."

# for문을 사용하여 10명까지 드려보자

# for i in range(1,11):
#     print("{0}번손님 반갑습니다".format(i))

# num = int(input())
# 
# if num == 0:
#     print("0입니다.")
# elif num % 2 == 0:
#     print("짝수 입니다.")
# else:
#     print("홀수입니다.")
# 
# for i in range(0,11):
#     print("현재"+str(i)+"값은 : ",end="")
#     if i == 0:
#         print("0입니다.")
#     elif i % 2 == 0:
#         print("짝수 입니다.")
#     else:
#         print("홀수입니다.")
        
# 우리가 계속 더해지는 숫자를 코딩하려합니다.
# 예를들어 x,y,z
# x는 제일 첫번째 숫자입니다.
# y는 계속해서 더해지는 숫자입니다.
# z는 몇번째 더해지는 숫자의 index입니다.
# x=1,y=2,z=5
# 1+2+2+2+2
# 9
# 등차수열이아함

# x = 10
# y = 5
# z = 125


# x, y, z = input().split()
# x = int(x)
# for i in range(int(z)-1):
#     x += int(y)
# print(x)
# # map(배열에 있는 형태를 하나하나 그대로 가져옴)
# num = list(map(int, input().split()))

# num = list(map(int, input().split()))
#
# for i in range(len(num)):
#     if num[i] > 11:
#         print("{0}은 500원 내세요".format(num[i]))

# 1 0 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# 0 0 0 0 1
# n x m
#  0 이 아닌 숫자를 카운트 해보자
# arr = []
# li = []
# for i in range(5):
#     for j in range(5):
#         if i == j:
#             li.append(1)
#         else:
#             li.append(0)
#     arr.append(li)
#     li = []
#
# for i in arr:
#     print(i)
# [1,2],[2,1],[3,3],[4,4]
# 단이는 배추 농사를 하려한다.
# 5 x 5 의 농장에 위의 값이 입력될경우 해당칸에는 1 반대는 0
# 을 출력하는 프로그램을 만들어보자
#
# arr = []
# li = []
# for i in range(5):
#     for j in range(5):
#         li.append(0)
#     arr.append(li)
#     li = []
#
# for i in val:
#     arr[i[0]][i[1]] = 1
#
# for i in arr:
#     print(i)
# val = [[1,2],[2,1],[3,3],[4,4]]
#
# farm = [[0 for _ in range(5)] for _ in range(5)]
#
# for i in val:
#     for j in i:
#         print(j,end=" ")
#     print()

val = [[1,2],[2,1],[3,3],[4,4]]

farm = [[0 for _ in range(5)] for _ in range(5)]

for i in val:
    farm[i[0]][i[1]] = 1

for i in farm:
    for j in i:
        print(j,end=" ")
    print()
arr = [1,4,2,45,5,7,32,0]
arr.sort()
arr.reverse()
print(arr)

