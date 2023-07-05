#https://www.acmicpc.net/problem/17298
n = int(input())
A = list(map(int,input().split()))

ans = [-1]*n
stack= [0]
for i in range(1,n):
    while stack:
        if A[stack[-1]] < A[i]:
            ans[stack.pop()] = A[i]
        else:
            break
    stack.append(i)
for i in ans:
    print(i,end=' ')