n, m = map(int, input().split())

mn = []
cnt = []

for i in range(n):
    mn.append(input())

for a in range(n-7):
    for b in range(m-7):
        w_start = 0
        b_start = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if mn[i][j] != 'W':
                        w_start += 1
                    else:
                        b_start += 1
                else:
                    if mn[i][j] != 'W':
                        b_start += 1
                    else: 
                        w_start += 1
        cnt.append(b_start)
        cnt.append(w_start)

print(min(cnt))

# 다시 풀어보기!
