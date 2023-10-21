n,k = map(int,input().split())
coins = []
dp = [0]*(k + 1)
dp[0] = 1
for i in range(n):
    coins.append(int(input()))

for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])