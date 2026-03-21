import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def BFS(x, y):
    q = [(x, y)]
    graph[x][y] = 0

    while q:
        x, y = q.pop(0)

        for i in range(4): # 탐색할 좌표를 변경하기 위한 x, y 좌표 설정
            nx = x + dx[i]  
            ny = y + dy[i]

            if not(0 <= nx < M and 0 <= ny < N): # 탐색할 좌표가 행렬 밖에 존재할 경우 넘어감
                continue

            if graph[nx][ny] == 1: # 탐색한 좌표가 1일 경우 0으로 변경 후 queue에 삽입
                q.append((nx, ny))
                graph[nx][ny] = 0


for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*N for i in range(M)] # 2차원 배열 초기화
    cnt = 0

    for _ in range(K): # 해당하는 좌표는 배추가 있음. 1로 값 변경
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                BFS(a, b)
                cnt += 1

    print(cnt)
    

