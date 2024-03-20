from sys import stdin
input = stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
INF = int(1e9)
# dp = [[INF] * (1 << n) for _ in range(n)]
dp = {}
# dp[cur][isVisit] -> 현재 cur 도시이며 방문현황은 isVisit과 같다는 뜻이고 아직 방문하지 않은 도시들을 모두 거쳐 시작점으로 돌아가는 최소비용을 값으로 가진다.

def dfs(x, isVisit):
    if isVisit == (1<<n) - 1: #모든 도시를 다 방무한경우 -> 11111 인 경우
        if graph[x][0]: # 출발점으로 가는 경로가 있을 때 -> x->0 경로가 있는지 판단하는 조건문
            return graph[x][0]
        else: # 출발점으로 가는 경로가 없을 때
            return INF
    if (x, isVisit) in dp: # 이미 최소 비용이 계산 되어있다면 -> INF 가 아니라면 계산된 적이 있다는 것
        return dp[(x, isVisit)]
    min_cost = INF
    for i in range(1,n):
        if not graph[x][i]: # 가능 경로가 없다면 -> graph[x][i] = 0 이라면 가는 경로가 없다는 것
            continue
        if isVisit & (1 << i): # 이미 방문한 도시라면 -> isVisit에는 방문한 도시가 1로 마스킹 되어있고 i번째 숫자가 1이면 방문 한것이기 때문에 isVisit과 i번째 숫자만 1인 수와 and 연산을 하면 0이상의 수가 나온다. 방문 하지 않았다면 0이 나온다.
            continue
        min_cost = min(min_cost, dfs(i, isVisit | (1 << i)) + graph[x][i])
        # dfs(i, isVisit | (1 << i)) => 다음 방문 노드는 i 이므로 x에 i 할당, i번째 노드를 방문 할 거니까 1번쨰 숫자를 1로 바꾸어 방문 처리
        # dfs(i, isVisit | (1 << i)) 의 결과는 isVisit의 도시를 방문한 상태이고 현재 i 번째 도시를 방문 했을 때 아직 방문하지 않은 도시를 거쳐 시작점으로 돌아가는 최소비용
    dp[(x, isVisit)] = min_cost
    return min_cost
print(dfs(0,1))