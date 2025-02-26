import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
edges = []

for i in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

distance = [INF] * (n + 1)

def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node, next_node, cost = edges[j]
            if distance[cur_node] != INF and distance[cur_node] + cost < distance[next_node]:
                distance[next_node] = distance[cur_node] + cost
                if i == n - 1:
                    return False
    return True

if bellman_ford(1):
    for i in range(2, n + 1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)