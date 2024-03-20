import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dp = [[0,1] for _ in range(n+1)]

def dfs(now):
    visited[now] = True
    for next in graph[now]:
        if visited[next]:
            continue
        dfs(next)
        dp[now][0] += dp[next][1]
        dp[now][1] += min(dp[next])
dfs(1)
print(min(dp[1]))