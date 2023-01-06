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
# print(edge.popleft())

# int find(int v[], int vNum)//정점이 속한 배열의 집합 번호를 가져오는 함수
# {
#     if (v[vNum] == -1)
#         return vNum;
#     while (v[vNum]!=-1)
#     {
#         vNum = v[vNum];
#     }
#     return vNum;
# }

# void union1(int v[], int vNum1, int vNum2)//집합을 합치는 함수
# {
#     int r1 = find(v, vNum1);//집합번호를 가져옴
#     int r2 = find(v, vNum2);//집합번호를 가져옴
#     v[r2] = r1;//v1집합의 번호로 합친다.
# }  