import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

g = [[0]*(N+1) for i in range(N+1)]

for i in range(M): 
    a, b = map(int, sys.stdin.readline().split())
    g[a][b] = g[b][a] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

def dfs(V):
    visited1[V] = 1
    print(V, end=' ')

    for i in range(1, N+1):
        if g[V][i] == 1 and visited1[i] == 0:
            dfs(i)


def bfs(V):
    q = [V]
    visited2[V] = 1

    while q:
        V = q.pop(0)
        print(V, end=' ')
        
        for i in range(1, N+1):
            if g[V][i] == 1 and visited2[i] == 0 :
                q.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)