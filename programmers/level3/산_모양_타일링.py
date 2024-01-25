def solution(n, tops):
    answer = 0
    ladder = [0] * (2 * n + 1)
    count = 2 * n + 1
    for i in range(len(tops)):
        if tops[i] == 1:
            ladder[2 * i + 1] = 1

    dp = [0] * count
    if ladder[1] == 1:
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2, count):
        if ladder[i] == 1:
            dp[i] = 2 + dp[i - 1] + dp[i - 2]
        else:
            dp[i] = 1 + dp[i - 2]
        dp[i] += dp[i - 1]
        dp[i] = dp[i] % 10007
    answer = (dp.pop() + 1) % 10007
    return answer