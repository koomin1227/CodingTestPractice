n = int(input())
nums = list(map(int, input().split()))

dp = [[i for i in nums] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + nums[i], dp[0][i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + nums[i])

print(max(max(dp[1]), max(dp[0])))