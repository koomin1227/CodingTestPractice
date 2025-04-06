from sys import stdin
INF = 3000000000
n, m = map(int, input().split())

dist = [[[INF,[]] for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i][0] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    dist[a - 1][b - 1][0] = c
    dist[a - 1][b - 1][1] += [a - 1 , b - 1]
    dist[b - 1][a - 1][0] = c
    dist[b - 1][a - 1][1] += [b - 1 , a - 1]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j][0] > dist[i][k][0] + dist[k][j][0]:
                dist[i][j][0] = dist[i][k][0] + dist[k][j][0]
                dist[i][j][1] = dist[i][k][1]

for i in range(n):
    for j in range(n):
        if dist[i][j][0] == 0:
            print('-', end = ' ')
        else:
            print(dist[i][j][1][1] + 1, end = ' ')
    print()


