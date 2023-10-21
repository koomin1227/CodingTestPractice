n,k = map(int,input().split())
coins = set()
dp = [k+1] * (k+1)

for i in range(n):
    coins.add(int(input()))
coins = list(coins)
dp[0] = 0
for i in coins:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
if dp[k] == k+1:
    print(-1)
else:
    print(dp[k])