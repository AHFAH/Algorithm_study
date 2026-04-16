N, M = map(int, input().split())

nums = list(map(int, input().split()))

start = 0
end = max(nums)

while start <= end:
    mid = (start+end) // 2
    m = 0

    for n in nums:
        if n > mid:
            m += n - mid
    
    if m < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)