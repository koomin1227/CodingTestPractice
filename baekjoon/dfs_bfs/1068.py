#https://www.acmicpc.net/problem/1068
from sys import stdin
input=stdin.readline

def dfs(tree,s,isVisit,tot):
    isVisit[s]=1
    #print(s,end=' ')
    cnt=0
    for i in tree[s]:
        if isVisit[i]==0:
            cnt+=1
            tot=dfs(tree,i,isVisit,tot)
    if cnt==0:
        tot+=1
    return tot

n=int(input())
tmp=list(map(int,input().split()))
tree=[[] for _ in range(n)]
isVisit=[0 for _ in range(n)]

r=int(input())
isVisit[r]=1
s=0
for i in range(0,n):
    if tmp[i]==-1:
        s=i
    else:
        tree[tmp[i]].append(i)
tot=0
if isVisit[s]==0:
    tot=dfs(tree,s,isVisit,tot)
print(tot)
# print(tree)
