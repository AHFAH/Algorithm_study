import sys

M = int(sys.stdin.readline())

s = set()

for i in range(M):
    cond = sys.stdin.readline().split()
    order = cond[0]

    if order == 'add':
        if cond[1] not in s:
            s.add(cond[1])
    elif order == 'remove':
        if cond[1] in s:
            s.remove(cond[1])
    elif order == 'check':
        if cond[1] in s:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        if cond[1] in s:
            s.remove(cond[1])
        else:
            s.add(cond[1])
    elif order == 'all':
        s.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif order == 'empty':
        s.clear()