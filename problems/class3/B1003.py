def fb_print(n):
    for i in range(2, n+1):
        fb[i] = [fb[i-1][0]+fb[i-2][0], fb[i-1][1]+fb[i-2][1]]


N = int(input())

fb = [[0, 0]] * 41
fb[0] = [1, 0]
fb[1] = [0, 1]

nums = []

for i in range(N):
    nums.append(int(input()))

fb_print(max(nums))

for i in nums:
    print(fb[i][0], fb[i][1])
