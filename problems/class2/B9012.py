N = int(input())

for i in range(N):
    ps = input()
    stack = []
    idx = 0
    flag = 0

    while idx < len(ps):
        if ps[idx] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                flag = 1
                break
            else:
                stack.pop()
        idx += 1
    
    if len(stack) == 0 and flag == 0:
        print("YES")
    else:
        print("NO")
