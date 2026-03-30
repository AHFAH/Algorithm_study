N = int(input())

nums = []
for i in range(N):
    nums.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max(nums)+1):
    dp[i] = dp[i-2] + dp[i-3]


for i in range(N):
    print(dp[nums[i]])

