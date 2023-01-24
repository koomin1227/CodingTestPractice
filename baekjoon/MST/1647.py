#https://www.acmicpc.net/problem/1647
from sys import stdin
from collections import deque
input=stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e=map(int,input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

# 간선을 입력받아 coat를 기준으로 오름차순 정렬
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
tot=[]
# 정렬된 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 두 노드의 루트 노드가 서로 다르다면 사이클이 발생하지 않은것이므로  
    if find_parent(parent, a) != find_parent(parent, b):
        # 신장 트리에 간선 추가
        union_parent(parent, a, b)
        result += cost
        tot.append(cost)
print(result-tot.pop())




