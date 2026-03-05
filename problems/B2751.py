import sys

a = int(input())

nums = []

for i in range(a):
    nums.append(int(sys.stdin.readline().strip()))

for i in sorted(nums):
    print(i)
