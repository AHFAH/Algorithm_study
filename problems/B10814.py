import sys

N = int(sys.stdin.readline())

member_list = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    member_list.append([int(age), name])

member_list.sort(key = lambda x : x[0])

for i in member_list:
    print(i[0], i[1])


# 다시 풀어보기!