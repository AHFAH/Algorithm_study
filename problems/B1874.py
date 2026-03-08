import sys

n = int(sys.stdin.readline())

seq = [] # 만들어야 할 수열
oper = [] # 수열을 만들기 위한 연산 과정
stack = [] 
max = 0 # stack에 push된 숫자의 최댓값
count = 0 # seq index
result = 1

for i in range(n):
    seq.append(int(sys.stdin.readline()))


while n > count:
    if max < seq[count]:
        for i in range(max, seq[count]):
            stack.append(i+1)
            oper.append("+")
        max = stack.pop()
        count += 1
        oper.append("-")
    else:
        if stack[len(stack)-1] == seq[count]:
            stack.pop()
            count += 1
            oper.append("-")
        else:
            print("NO")
            result = 0
            break

if result == 1:
    for i in oper:
        print(i)

    