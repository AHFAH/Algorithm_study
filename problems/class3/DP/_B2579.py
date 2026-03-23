import sys

n = int(sys.stdin.readline())

nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline()))

dp = [0] * (n)

if n <= 2:
    print(sum(nums))
else:
    dp[0] = nums[0]
    dp[1] = nums[0]+ nums[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3]+nums[i-1]+nums[i], dp[i-2]+nums[i])
    
    print(dp[n-1])
