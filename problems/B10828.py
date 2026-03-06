import sys

N = int(sys.stdin.readline())

s = []

for i in range(N):
    cond = sys.stdin.readline().split()
    order = cond[0]

    if order == 'push':
        s.append(cond[1])
    
    elif order == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    
    elif order == 'size':
        print(len(s))

    elif order == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[len(s)-1])