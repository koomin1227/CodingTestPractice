# https://www.acmicpc.net/problem/1874
from sys import stdin
input=stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
stack = [0]
cur = 1
ans = []
for num in nums:
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    elif cur <= num:
        for i in range(cur,num + 1):
            stack.append(cur)
            cur += 1
            ans.append('+')
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        ans = []
        break
if len(ans) != 0:
    for i in ans:
        print(i)