import sys

K, N = map(int, sys.stdin.readline().split())
nums = []

for i in range(K):
    nums.append(int(sys.stdin.readline()))

start = 1
end = max(nums)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for n in nums:
        count += n // mid
    
    if count < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)