import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
count_w = 0  
count_b = 0


def dc(r, c, N):
    global count_w, count_b
    color = paper[r][c]
    for i in range(r, r+N):
        for j in range(c, c+N):
            if color != paper[i][j]:
                m = N//2
                dc(r, c, m)
                dc(r, c+m, m)
                dc(r+m, c, m)
                dc(r+m, c+m, m)
                return
            
    if color == 0:
        count_w += 1
    else:
        count_b += 1


dc(0, 0, N)
print(count_w)
print(count_b)