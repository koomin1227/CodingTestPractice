#https://www.acmicpc.net/problem/1469
from sys import stdin
input=stdin.readline
n=int(input())
Nset=list(map(int,input().split()))
Nset.sort(reverse=True)
result=[0 for _ in range(2*n)]
answer=[]
ans=0
def check(i,x):
    if result[i]==0 and i+Nset[x]+1<2*n and result[i+Nset[x]+1]==0:
        return True
    else:
        return False
def dfs(x):
    global ans
    if x==len(Nset):
        answer.append(result[:])
        ans=1
    else:
        for i in range(2*n):
            if check(i,x):
                result[i]=Nset[x]
                result[i+Nset[x]+1]=Nset[x]
                if dfs(x+1)==0:
                    return 0
                result[i]=0
                result[i+Nset[x]+1]=0

dfs(0)
if ans==0:
    print('-1')
else:
    answer.sort()
    for i in range(2*n):
        print(answer[0][i],end=' ')


