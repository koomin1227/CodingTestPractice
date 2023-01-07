#https://www.acmicpc.net/problem/1197
from sys import stdin
from collections import deque
input=stdin.readline

v,e=map(int,input().split())
vSet=[-1 for _ in range(v+1)]
ed=[]
for i in range(e):
    a,b,c=map(int,input().split())
    ed.append([c,a,b])
ed.sort()
edge=deque(ed)
ecnt=0
etot=0
def find(vNum):
    if vSet[vNum]==-1:
        return vNum
    while vSet[vNum]!=-1:
        vNum=vSet[vNum]
    return vNum

while ecnt<v-1:
    tmp=edge.popleft()
    vnum1=find(tmp[1])
    vnum2=find(tmp[2])
    if vnum1!=vnum2:
        ecnt+=1
        etot+=tmp[0]
        vSet[vnum2]=vnum1
print(etot)