from sys import stdin
input = stdin.readline

n = int(input())
passenger_car = list(map(int, input().split()))
max_passenger_car = int(input())

cumulative_sum = [0]
total = 0
for i in range(n):
    total += passenger_car[i]
    cumulative_sum.append(total)

dp = [[0] * (n + 1) for _ in range(4)]
for i in range(1, 4):
    for j in range(max_passenger_car * i, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_passenger_car] + (cumulative_sum[j] - cumulative_sum[j - max_passenger_car]))

print(dp[3].pop())