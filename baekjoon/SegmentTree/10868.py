from sys import stdin
from math import ceil, log
input = stdin.readline

def segment(left, right, i):
    if left == right:
        segment_tree[i] = nums[left]
        return segment_tree[i]
    mid = (right + left) // 2
    # 최소 최대 계산 로직
    left_min = segment(left, mid, i*2)
    right_min = segment(mid + 1, right, i*2 + 1)
    segment_tree[i] = min(left_min, right_min)

    return segment_tree[i]

def interval_sum(start, end, idx, interval_left, interval_right):
    if interval_left > end or interval_right < start:
        return 1000000001
    if interval_left <= start and interval_right >= end:
        return segment_tree[idx]
    mid = (start + end) // 2
    left_min = interval_sum(start,mid, idx * 2, interval_left, interval_right)
    right_min = interval_sum(mid + 1,end, idx * 2 + 1, interval_left, interval_right)
    minimum = min(left_min, right_min)
    return minimum


n, m = map(int, input().split())
nums = []
oper = []
for i in range(n):
    nums.append(int(input()))
for i in range(m):
    oper.append(list(map(int, input().split())))

H = ceil(log(len(nums), 2))
tree_size = pow(2, H+1) - 1
segment_tree = [0] + [0] * tree_size
segment(0, len(nums) - 1, 1)

for a,b in oper:
    mini = interval_sum(0, len(nums) - 1, 1, a - 1, b - 1)
    print(mini)
