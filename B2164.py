from collections import deque

q = deque()

a = int(input())

for i in range(a):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])