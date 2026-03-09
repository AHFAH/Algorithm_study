import sys

N = int(sys.stdin.readline())
nums = []
count = {}

for i in range(N):
    n = int(sys.stdin.readline())
    nums.append(n)
    count.setdefault(n, 0)
    count[n] += 1

nums.sort()


max_value = max(count.values())
keys = []
for i in set(nums):
    if count[i] == max_value:
        keys.append(i)

keys.sort()

print(round(sum(nums)/N))
print(nums[N//2])
print(keys[0] if len(keys) == 1 else keys[1])
print(nums[N-1] - nums[0])