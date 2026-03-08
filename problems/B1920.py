N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

is_exist = {}
for i in A:
    is_exist[i] = 1

for i in B:
    if is_exist.get(i) == None:
        print(0)
    else:
        print(1)




