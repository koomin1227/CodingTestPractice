#https://www.acmicpc.net/problem/1939
from sys import stdin
from collections import deque
input=stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
right = 0
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    right = max(right, c)
s,e = map(int,input().split())

left = 1

def count(target):
    que = deque()
    que.append(s)
    is_visit = [0]*(n+1)
    is_visit[s] = 1
    while (que):
        now = que.popleft()
        for b,c in graph[now]:
            if is_visit[b] == 0 and c >= target:
                is_visit[b] = 1
                que.append(b)
    if is_visit[e] == 1:
        return True
    else:
        return False

while left <= right:
    mid = (left + right)//2

    is_reachable = count(mid)
    if is_reachable:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)
