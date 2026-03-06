N = int(input())

lst = []

for i in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])

for i in sorted(lst):
    print(i[0], i[1])