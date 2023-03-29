#https://www.acmicpc.net/problem/1082
from sys import stdin
input=stdin.readline

n = int(input())
p = list(map(int,input().split()))
m = int(input())
ans = []

min_0_i = p.index(min(p))
min_0_p = min(p)
min_1_i = -1
if min_0_i == 0 and n > 1:
    min_1_p = min(p[1:])
    min_1_i = p.index(min(p[1:]))
if min_1_i != -1 and m >= min_1_p:
    ans.append(min_1_i)
    m = m - min_1_p
while(1):
    if m >= min_0_p:
        ans.append(min_0_i)
        m=m - min_0_p
    else:
        break
for i in range(len(ans)):
    for j in range(n-1,ans[i],-1):

        if m+p[ans[i]] >= p[j]:
            m = m + p[ans[i]] - p[j]
            ans[i] = j
            break
print(int(''.join(map(str, ans))))
            


