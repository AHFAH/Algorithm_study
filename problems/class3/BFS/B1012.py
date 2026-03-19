import sys
from collections import deque

T = int(sys.stdin.readline())
N, M, K = map(int, sys.stdin.readline().split())

for t in range(T):
    graph = [[0]*N for i in range(M)] # 2차원 배열 초기화

    for _ in range(K): # 해당하는 좌표는 배추가 있음. 1로 값 변경
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1
    

