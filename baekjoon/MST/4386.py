# https://www.acmicpc.net/problem/4386
from sys import stdin
import math
import heapq
input = stdin.readline

n = int(input())
coordinate = []
isVisit = [0] * n
for _ in range(n):
    x,y = map(float, input().split())
    coordinate.append((x,y))
def extractEdge(start):
    edges = []
    start_x, start_y = coordinate[start]
    for i in range(n):
        if start == n:
            continue
        target_x, target_y = coordinate[i]
        weight = math.sqrt((start_x - target_x)**2 + (start_y - target_y)**2)
        edges.append([weight, start,i])
    return edges

isVisit[0] = 1
adjacent_edge = extractEdge(0)
heapq.heapify(adjacent_edge)
total_weight = 0
while adjacent_edge:
    w, s, e = heapq.heappop(adjacent_edge)
    if isVisit[e] == 0:
        isVisit[e] = 1
        total_weight += w
        for edge in extractEdge(e):
            if isVisit[edge[2]] == 0:
                heapq.heappush(adjacent_edge, edge)


print(round(total_weight, 2))