from sys import stdin
import heapq
input = stdin.readline
n, m = map(int, input().split())
infos = []
graph = [[] for i in range(n+1)]
inOrder = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    inOrder[b] += 1
    graph[a].append(b)
que=[]
for i in range(1,n+1):
    if inOrder[i]==0:
        heapq.heappush(que, i)
ans = []
while que:
    x = heapq.heappop(que)
    ans.append(x)
    # print(x, end=' ')
    for i in graph[x]:
        inOrder[i] -= 1
        if inOrder[i] == 0:
            heapq.heappush(que, i)
print(' '.join([str(i) for i in ans]))