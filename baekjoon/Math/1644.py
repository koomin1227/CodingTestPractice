import math
from sys import stdin
input = stdin.readline
n = int(input())
def get_primes(x):
    nums = [True] * (x + 1)
    for i in range(2, int(math.sqrt(x) + 1)):
        if nums[i] == True:
            for j in range(i+i, x+1,i):
                nums[j] = False
    primes = [i for i in range(2, x+1) if nums[i] == True]
    # print(primes)
    return primes
primes = get_primes(n) + [0]
start = 0
end = 0
ans = 0
# mid = n//2 + 1
prime_sum = 2
while end < len(primes) - 1:
    # prime_sum = sum(primes[start:end+1])
    if prime_sum == n:
        ans+= 1
        prime_sum -= primes[start]
        start += 1
        end += 1
        prime_sum += primes[end]
    elif prime_sum < n:
        end += 1
        prime_sum += primes[end]
    else:
        prime_sum -= primes[start]
        start += 1
    
print(ans)