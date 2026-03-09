N, K = map(int, input().split())
idx = 0
num_list = list(range(1, N+1))
result = []

while len(num_list) > 0:
    idx += K-1
    idx = idx % len(num_list)
    result.append(num_list.pop(idx))

print("<", end="")
print(*result, sep=", ", end="")
print(">", end="")