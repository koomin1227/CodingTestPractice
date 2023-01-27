#https://www.acmicpc.net/problem/1987
from sys import stdin
input=stdin.readline
dr=[1,0,-1,0]
dc=[0,1,0,-1]
Rr,Cc=map(int,input().split())
board=[]
for i in range(Rr):
    board.append(input())
isvisited=[]
isvisited2=[[0]*(Cc)for _ in range(Rr)]
dic=[0]*26
maxi=0
tot=0
def dfs(r,c):
    global tot,maxi
    if dic[ord(board[r][c])-ord('A')] !=1:
        tot+=1
        isvisited.append(board[r][c])
        dic[ord(board[r][c])-ord('A')]=1
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if (nr>=0 and nr<Rr) and (nc>=0 and nc<Cc):
                dfs(nr,nc)
        maxi=max(maxi,tot)
        tot-=1
        dic[ord(isvisited.pop())-ord('A')]=0
dfs(0,0)   
print(maxi)