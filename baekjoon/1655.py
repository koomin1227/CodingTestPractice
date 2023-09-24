# https://www.acmicpc.net/problem/1655
from sys import stdin
import heapq
input=stdin.readline

left_heap = []
right_heap = []
ans = []
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
for i in range(n):
    num = nums[i]
    if i % 2 == 0:
        heapq.heappush(left_heap, num * -1)
    elif i % 2 == 1:
        heapq.heappush(right_heap, num)
    if i > 0 and left_heap[0]*-1 > right_heap[0]:
        tmp_l = heapq.heappop(left_heap) * -1
        tmp_r = heapq.heappop(right_heap) * -1
        heapq.heappush(right_heap, tmp_l)
        heapq.heappush(left_heap, tmp_r)
    ans.append(left_heap[0] * -1)
for i in ans:
    print(i)
