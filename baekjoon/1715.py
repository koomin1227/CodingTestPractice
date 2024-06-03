from sys import stdin
import heapq
input = stdin.readline

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
tot = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    tot += a+b
    heapq.heappush(heap, a+b)

print(tot)