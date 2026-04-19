N = int(input())

fruit = list(map(int, input().split()))

fruit_set = len(set(fruit))
num = 0

if fruit_set <= 2:
    print(N)
else:
    for a in range(N-1):
        for b in range(N-1-a):
            f = fruit[a:N-b]
            if len(set(f)) <= 2:
                num = max(num, len(f))
    
    print(num)

