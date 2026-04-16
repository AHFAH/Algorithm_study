import sys

N, M, B = map(int, sys.stdin.readline().split())

g = []
for i in range(N):
    g.append(list(map(int, sys.stdin.readline().split())))

time = int(1e9)
height = 0

for i in range(257):
    high, low = 0, 0
    for a in range(N):
        for b in range(M):
            h = g[a][b]
            
            if h > i:
                high += h - i
            else:
                low += i - h
    
    if high + B < low:
        continue

    t = high * 2 + low
    
    if t <= time:
        time = t
        height = i

print(time, height, sep=" ")