import sys
sys.setrecursionlimit(500000000)
input = sys.stdin.readline
n, r1, r2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

is_visit = [False] * (n + 1)
is_visit[r1] = True

def dfs(cur, costs, target):
    if cur == target:
        costs.append(-1)
        return costs
    for node in graph[cur]:
        if is_visit[node[0]]:
            continue
        is_visit[node[0]] = True
        costs.append(node[1])
        result = dfs(node[0], costs, target)
        if result[-1] == -1:
            return costs
        costs.pop()
    return costs

course = dfs(r1, [], r2)
course.pop()

if len(course) == 0:
    print(0)
else:
    print(sum(course) - max(course))