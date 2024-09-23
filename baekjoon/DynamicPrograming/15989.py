t = int(input())

cases = []

for _ in range(t):
    cases.append(int(input()))

for case in cases:
    dp = [1] * (case + 1)
    for i in range(2, case + 1):
        dp[i] = dp[i] + dp[i - 2]
    for i in range(3, case + 1):
        dp[i] = dp[i] + dp[i - 3]
    print(dp[case])