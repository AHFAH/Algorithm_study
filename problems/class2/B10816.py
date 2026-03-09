import sys

N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

count = {}
for i in N_lst:
    count.setdefault(i, 0)
    count[i] += 1

result = []

for i in M_lst:
    if count.get(i) == None:
        result.append(0)
    else:
        result.append(count.get(i))

for i in result:
    print(i, end=" ")