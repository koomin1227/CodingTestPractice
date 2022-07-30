from sys import stdin
from collections import deque
n,l,r=map(int,stdin.readline().split())
land=[]
dx=[-1,0,1,0]#uldr
dy=[0,-1,0,1]
for i in range(n):
    land.append(list(map(int,stdin.readline().split())))
#연합처리 함수
def dfs(x,y,day):
    num=0
    tot=0
    com=[]
    que=deque()
    que.append([x,y])
    com.append([x,y])
    if visited[x][y]==day:
        return False
    visited[x][y]=day
    while que:
        c=que.popleft()
        num+=1
        tot+=land[c[0]][c[1]]
        
        nx=c[0]+dx[0]
        ny=c[1]+dy[0]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visited[nx][ny]!=day and (abs(land[c[0]][c[1]]-land[nx][ny])>=l and abs(land[c[0]][c[1]]-land[nx][ny])<=r):
                que.append([nx,ny])
                com.append([nx,ny])
                visited[nx][ny]=day
        nx=c[0]+dx[1]
        ny=c[1]+dy[1]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visited[nx][ny]!=day and (abs(land[c[0]][c[1]]-land[nx][ny])>=l and abs(land[c[0]][c[1]]-land[nx][ny])<=r):
                que.append([nx,ny])
                com.append([nx,ny])
                visited[nx][ny]=day
        nx=c[0]+dx[2]
        ny=c[1]+dy[2]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visited[nx][ny]!=day and (abs(land[c[0]][c[1]]-land[nx][ny])>=l and abs(land[c[0]][c[1]]-land[nx][ny])<=r):
                que.append([nx,ny])
                com.append([nx,ny])
                visited[nx][ny]=day
        nx=c[0]+dx[3]
        ny=c[1]+dy[3]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visited[nx][ny]!=day and (abs(land[c[0]][c[1]]-land[nx][ny])>=l and abs(land[c[0]][c[1]]-land[nx][ny])<=r):
                que.append([nx,ny])
                com.append([nx,ny])
                visited[nx][ny]=day



    if num>=2:
        tot=tot//num
        for i in com:
            land[i[0]][i[1]]=tot
        return True
    elif num==1:
        return False

visited=[[0]*n for _ in range(n)]
check=False
for day in range(1,2002):
    for i in range(0,n):
        for j in range(0,n):
            t=dfs(i,j,day)
            if t:
                check=True 
    if check==False:
        break
    check=False
print(day-1)


