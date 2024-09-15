from sys import stdin
input = stdin.readline
n = input()
nums = [int(i) for i in list(n)[:-2]]
dp = [1] + [0] * (len(nums))
dp[1] = 1
is_decode = True
if nums[0] == 0:
    is_decode = False
for i in range(2, len(dp)):
    if nums[i - 1] > 0:
        dp[i] = dp[i-1]
    if nums[i-2] * 10 + nums[i - 1] <= 26 and nums[i-2] * 10 + nums[i - 1] >= 10:
        dp[i] += dp[i-2]

if is_decode:
    print(dp[-1]%1000000)
else:
    print(0)