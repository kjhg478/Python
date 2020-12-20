#프로그램을 만들건데
#온도에 따라서 걱정을 해주는 로봇
#ex) 25도가 넘어가면 로봇이 (너무 더워요 집에 있어요)
#ex) 10~25도 사이면 로봇이 (날씨가 좋아요 나가도 될 거 같아요)
#ex) 0~10도 사이면 로봇이 (날씨가 추워요 외투를 입어주세요)
#ex) 0도 이하면 로봇이 (밖에 너무 추워요 나가지마요)
#ex) 총 3번의 값 25, 10, -1

arr = list(map(int,input().split(' ')))

for i in arr:
    if i > 25:
        print("너무 더워요 집에 있어요")
    elif 10 <= i <= 25:
        print("날씨가 좋아요 나가도 될 거 같아요")
    elif 0 <= i < 10:
        print("날씨가 추워요 외투를 입어주세요")
    elif i < 0:
        print("밖에 너무 추워요 나가지마요")

# arr = list(map(int,input().split(' ')))
# for i in arr:
#     print(i)


arr = list(map(int, input().split(' ')))
for i in arr:
    if arr[0] == i:
        print("너무 더워요 집에 있어요")
    elif arr[1] == i:
        print("날씨가 추워요 외투를 입어주세요")
    elif arr[2] == -1:
        print("밖에 너무 추워요 나가지마요")

arr = list(map(int, input().split(' ')))
for i in arr:
    if i == 25:
        print("너무 더워요 집에 있어요")
    elif i == 10:
        print("날씨가 추워요 외투를 입어주세요")
    elif i == -1:
        print("밖에 너무 추워요 나가지마요")

