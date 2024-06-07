from sys import stdin
from itertools import permutations, combinations, combinations_with_replacement
import heapq
input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
p , q = map(int, input().split())

ns = []
divisions = []
for i in range(1, n+1):
    ns.append(i)
a = combinations_with_replacement(ns, (q + 1))
for i in a:
    if sum(i) == n:
        divisions.append(i)

max_num = 0
for p in permutations(nums, n):
    tot = 1
    s = 0
    for division in divisions:
        tot = 1
        s = 0
        for j in division:
            tot *= sum(p[s : s + j])
            s = s + j
        max_num = max(tot, max_num)


print(max_num)