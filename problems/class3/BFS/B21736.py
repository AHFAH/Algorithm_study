import sys

N, M = map(int, sys.stdin.readline().split())
count = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

g = []
a, b = 0, 0

for i in range(N):
    s = sys.stdin.readline().strip()
    g.append(list(s[::1]))

for i in range(N):
    for j in range(M):
        if g[i][j] == 'I':
            a = i
            b = j
            break

visited = [[0]*(M) for i in range(N)]


q = [(a, b)]
while q:
    x, y = q.pop(0)
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < N and 0 <= ny < M):
            continue

        if g[nx][ny] == 'O' and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = 1
        elif g[nx][ny] == 'P' and visited[nx][ny] == 0:
            q.append((nx, ny))
            count += 1
            visited[nx][ny] = 1

if count > 0:
    print(count)
else: 
    print("TT")
