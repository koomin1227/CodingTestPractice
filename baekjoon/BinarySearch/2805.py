# https://www.acmicpc.net/problem/2805
from sys import stdin
input=stdin.readline

n,m = map(int, input().split())
trees = list(map(int, input().split()))

max_h = max(trees)
right = max_h
left = 0
def check(h):
    tree_sum = 0
    for tree in trees:
        if tree > h:
            tree_sum += (tree - h)
    return tree_sum
ans = -1
while (right>=left):
    mid = (right + left) // 2
    cur_sum = check(mid)
    if cur_sum >= m and (check(mid+1) < m or mid == max_h):
        ans = mid
        break
    elif cur_sum > m:
        left = mid + 1
    elif cur_sum < m:
        right = mid - 1

print(ans)

