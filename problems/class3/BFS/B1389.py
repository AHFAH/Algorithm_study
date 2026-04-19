import sys


N, M = map(int, sys.stdin.readline().split())
net = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

bacon = [0] * (N+1) # 각 유저의 케빈 베이컨 수를 저장할 리스트
bacon[0] = int(1e9)
 
def bfs(v):
    visited = [0] * (N+1)
    depth = [0] * (N+1) # 각 노드(유저)의 탐색 깊이를 저장할 리스트

    q = [v]
    visited[v] = 1 

    while q:
        V = q.pop(0)
        
        for i in net[V]:
            if visited[i] == 0:
                depth[i] = depth[V] + 1 # 자신의 윗 노드의 깊이에서 1 더함
                q.append(i)
                visited[i] = 1
    
    return sum(depth) # 각 노드의 depth를 다 더하면 케빈 베이컨 수가 나옴

for i in range(1, N+1):
    bacon[i] = bfs(i)


for i in range(1, N+1):
    if min(bacon) == bacon[i]:
        print(i)
        break