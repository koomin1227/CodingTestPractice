from sys import stdin
from math import ceil, log
input = stdin.readline

def segment(left, right, i):
    if left == right:
        segment_tree[i] = nums[left]
        return segment_tree[i]
    mid = (right + left) // 2
    segment_tree[i] = segment(left, mid, i*2) + segment(mid + 1, right, i*2 + 1)
    return segment_tree[i]

def interval_sum(start, end, idx, interval_left, interval_right):
    if interval_left > end or interval_right < start:
        return 0
    if interval_left <= start and interval_right >= end:
        return segment_tree[idx]
    mid = (start + end) // 2
    return interval_sum(start,mid, idx * 2, interval_left, interval_right) + interval_sum(mid + 1,end, idx * 2 + 1, interval_left, interval_right)

def update(start, end, node, idx, val):
    if start > idx or idx > end:
        return segment_tree[node]
    segment_tree[node] += val - nums[idx]
    if start != end:
        mid = (start + end) // 2
        update(start ,mid, node*2, idx,val)
        update(mid + 1 ,end, node*2 + 1, idx,val)


n, q = map(int, input().split())

oper = []
nums = list(map(int, input().split()))
for i in range(q):
    oper.append(list(map(int, input().split())))

H = ceil(log(len(nums), 2))
tree_size = pow(2, H+1) - 1
segment_tree = [0] + [0] * tree_size
segment(0, len(nums) - 1, 1)

for x,y,a,b in oper:
    if x <= y:
        inter_sum = interval_sum(0, len(nums) - 1, 1, x - 1, y - 1)
        print(inter_sum)
    else:        
        inter_sum = interval_sum(0, len(nums) - 1, 1, y - 1, x - 1)
        print(inter_sum)

    update(0, len(nums) - 1, 1, a - 1, b)
    nums[a-1] = b
