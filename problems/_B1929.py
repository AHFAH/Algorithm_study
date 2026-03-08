import math

m, n = map(int, input().split())

is_prime = [True for i in range(n+1)]
is_prime[1] = False

for i in range(2, int(n**(1/2)+1)):
    if is_prime[i]:
        for j in range(i*2, n+1, i):
            is_prime[j] = False
            
prime_nums = [x for x in range(m, n+1) if is_prime[x]]

for i in prime_nums:
    print(i)


# 다시 풀어보기!