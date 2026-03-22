import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = [[] for i in range(N+1)]

for i in range(M): 
    a, b = map(int, sys.stdin.readline().split()) # 각 컴퓨터를 서로 연결, 노드 연결
    net[a].append(b)
    net[b].append(a)


def bfs():
    q = deque()
    count = 0
    q.append(1)
    visited[1] = True # 1번 컴퓨터에서 시작하므로 queue에 1번 넣어줌
    while q: # 1번 컴퓨터와 연결된 모든 노드들을 방문
        cur = q.popleft()
        for val in net[cur]:
            if visited[val] == False: # Fasle인 경우 방문된 적 없으므로 queue에 넣어줌
                q.append(val)
                visited[val] = True
                count += 1 # 새로운 컴퓨터에 들렀으므로 감염된 컴퓨터 수 증가

    print(count)

visited = [False for i in range(N+1)]
bfs()