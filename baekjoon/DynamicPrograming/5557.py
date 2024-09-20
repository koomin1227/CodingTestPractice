n = int(input())
nums = [int(i) for i in list(map(int,input().split()))]
target = nums.pop()

dp = [[0] * 21 for _ in range(len(nums))]
dp[0][nums[0]] = 1

for i in range(1, len(nums)):
    for j in range(21):
        if dp[i - 1][j] != 0:
            num = nums[i]
            if j + num >= 0 and j + num <= 20:
                dp[i][j + num] += dp[i - 1][j]
            if j - num >= 0 and j - num <= 20:
                dp[i][j - num] += dp[i - 1][j]  

print(dp[-1][target])