import sys


N, M = map(int, sys.stdin.readline().split())

names = []
count = {}

for i in range(N+M):
    name = sys.stdin.readline().rstrip()
    names.append(name)
    count.setdefault(name, 0)
    count[name] += 1

lst = []
names = set(names)

for i in names:
    if count.get(i) == 2:
        lst.append(i)

print(len(lst))
lst.sort()

for i in range(len(lst)):
    print(lst[i])
