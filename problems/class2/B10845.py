import sys

N = int(sys.stdin.readline())
nums = []

for i in range(N):
    cond = sys.stdin.readline().split()
    oper = cond[0]

    if oper == 'push':
        nums.append(cond[1])
    elif oper == 'front':
        if len(nums) != 0:
            print(nums[0])
        else:
            print(-1)
    elif oper == 'back':
        if len(nums) != 0:
            print(nums[len(nums)-1])
        else:
            print(-1)
    elif oper == 'pop':
        if len(nums) != 0:
            print(nums.pop(0))
        else:
            print(-1)
    elif oper == 'size':
        print(len(nums))
    else:
        if len(nums) == 0:
            print(1)
        else:
            print(0)