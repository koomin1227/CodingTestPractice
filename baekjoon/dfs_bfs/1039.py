#https://www.acmicpc.net/problem/1039
from collections import deque
from sys import stdin
input=stdin.readline

def to_int(num):
    res = 0
    for i in num:
        res = (res * 10) + int(i)
    return res

n,k=map(int,input().split())
visited = set()
n_str=str(n)
m = len(n_str)
visited.add((n_str, 0))
que = deque()
que.append([n_str, 0])
last_k=0
max_n = 0
while que:
    cur = que.popleft()
    last_k = cur[1]
    if cur[1] == k:
        max_n = max(max_n, int(cur[0]))
        continue
    n_list=list(cur[0])
    for i in range(m-1):
        for j in range(i+1,m):
            if not (n_list[j] == '0' and i == 0):
                n_list[i],n_list[j] = n_list[j],n_list[i]
                num = to_int(n_list)
                if (str(num),cur[1]+1) not in visited:
                    visited.add((str(num),cur[1]+1))
                    que.append([str(num),cur[1]+1])
                n_list[i],n_list[j] = n_list[j],n_list[i]
if last_k != k:
    print(-1)
else:
    print(max_n)