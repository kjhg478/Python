
# 한자리 숫자가 입력이 됩니다.
# 랜덤으로 입력이 되는데 0~9 값이 5자리가 입력이 됩니다.
# 사용자는 연산을 할 수 있는데 단 두가지만 할 수 있습니다. + *
# 한자릿수 마다 연산을 하는데 가장 큰 수를 구하는 프로그램을 작성하시오
# str 객체를 하나하나별로 기억하지만 int일때는 숫자를 전체로 기억
arr = input()
result = 0

for i in range(len(arr)):
    i = int(arr[i])
    if result <= 1 or i <=1:
        result += i
    else:
        result *= i
print(result)