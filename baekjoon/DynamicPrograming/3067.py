from sys import stdin
input = stdin.readline
T = int(input())
answer = []
for t in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], m+1):
            dp[j] += dp[j - coins[i]]
    
    answer.append(dp[m])

for i in answer:
    print(i)