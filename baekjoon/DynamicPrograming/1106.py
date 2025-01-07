c, n = map(int, input().split())
num = float('INF')
marketing = []
for _ in range(n):
    marketing.append(list(map(int, input().split())))

dp = [num for _ in range(c+100)]
dp[0] = 0
for cost, customer in marketing:
    for i in range(customer, c+100):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[c:]))