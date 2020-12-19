# 리스트 []
# 지하철 칸 별로 10명, 20명, 30명
subway = [10, 20, 30]
subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

# 하하가 다음칸에 탐
subway.append("하하")
print(subway)

# 정형돈은 유재석 조세호 사이
subway.insert(1,"정형돈")
print(subway)

# 한명씩 뒤에서 빼냄
subway.pop()
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("정형돈")
print(subway.count("정형돈"))

# 정렬 가능
num_list = [5,2,4,2,1]
num_list.sort()
print(num_list)

# 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양항 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)
num_list.extend(mix_list)
print(num_list)
