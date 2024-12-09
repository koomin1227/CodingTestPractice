n = int(input())
graph = [[] for i in range(n + 1)]
times = [0]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    times.append(tmp[0])
    if tmp[1] == 0:
        dp[i] = times[i]
    for j in tmp[2:]:
        graph[j].append(i)

for i in range(1, n + 1):
    for j in graph[i]:
        dp[j] = max(dp[j], dp[i] + times[j])
        

print(max(dp))