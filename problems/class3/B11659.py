import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
sum = 0
sums = [0]

for i in range(N):
    sum += arr[i]
    sums.append(sum)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(sums[b] - sums[a-1])