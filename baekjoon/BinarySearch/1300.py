# https://www.acmicpc.net/source/66719569
from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())

left = 0
right = n*n

def countLessThanN(num):
    cnt = 0
    for i in range(1,n + 1):
        cnt += min(num//i,n)
    return cnt

while (left <= right):
    mid = (left + right) // 2
    cnt = countLessThanN(mid)
    if (cnt < k):
        left = mid + 1
    else:
        ans = mid
        right = mid-1

print(ans)