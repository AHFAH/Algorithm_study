import sys


N, M = map(int, sys.stdin.readline().split())
net = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

count = 0
visited = [0] * (N+1)


def dfs(n):
    visited[n] = 1
    stack = [n]

    while stack:
        node = stack.pop()
        for i in net[node]:
            if visited[i] == 0:
                visited[i] = 1
                stack.append(i)


for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)