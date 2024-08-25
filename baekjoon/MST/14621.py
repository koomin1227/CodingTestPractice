from sys import stdin
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
school_kind = list(input().split())

for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    if (school_kind[a - 1] != school_kind[b - 1]):
        edges.append((cost, a, b))

edges.sort()
tot=[]
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        tot.append(cost)
if len(tot) != v-1:
    print(-1)
else:
    print(result)
