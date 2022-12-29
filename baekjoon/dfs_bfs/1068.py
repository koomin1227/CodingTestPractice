#https://www.acmicpc.net/problem/1068
from sys import stdin
input=stdin.readline

def dfs(tree,s,isVisit,tot):
    isVisit[s]=1
    cnt=0
    for i in tree[s]:
        if isVisit[i]==0:
            cnt+=1
            tot=dfs(tree,i,isVisit,tot)
    if cnt==0:
        tot+=1
    return tot
#입력
n=int(input())
tmp=list(map(int,input().split()))
r=int(input())
#준비
tree=[[] for _ in range(n)]
isVisit=[0 for _ in range(n)]
isVisit[r]=1
s=0
for i in range(0,n):
    if tmp[i]==-1:
        s=i
    else:
        tree[tmp[i]].append(i)
#알고리즘
tot=0
if isVisit[s]==0:
    tot=dfs(tree,s,isVisit,tot)
#출력
print(tot)

