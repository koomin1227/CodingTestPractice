n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

dp = [1] * n
dp[1] = 1

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
