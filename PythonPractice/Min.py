# n, k = map(int,input().split(' '))
# arr = []
# count = 0
# for i in range(n):
#     arr.append(int(input()))
# for i in range(n):
#     count = count + k // arr[-1-i]
#     k = k % arr[-1-i]
#
# print(count)

n, k = map(int,input().split(' '))
arr = []
count = 0
for i in range(n):
    arr.append(int(input()))

arr.sort()
print(arr)

for i in range(n):
    count = count + k // arr[i]
    k = k % arr[i]

print(count)