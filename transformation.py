from sys import stdin
import copy
n=int(stdin.readline())
s=list(map(int,stdin.readline().split()))                                                                                                                                                  
oper=list(map(int,stdin.readline().split()))
mi=1000000001
ma=-1000000001
def dfs(x,oper,tot):
    if oper[0]!=0:
            oper[0]-=1
            dfs(x+1,oper,tot+s[x+1])
            oper[0]+=1
    if oper[1]!=0:
            oper[1]-=1
            dfs(x+1,oper,tot-s[x+1])
            oper[1]+=1
    if oper[2]!=0:
            oper[2]-=1
            dfs(x+1,oper,tot*s[x+1])
            oper[2]+=1
    if oper[3]!=0:
            oper[3]-=1
            if tot>0:
                dfs(x+1,oper,tot//s[x+1])
            else:
                dfs(x+1,oper,((tot*-1)//s[x+1])*-1)
            oper[3]+=1
    if (x==n-1):
        global mi
        global ma
        if mi>tot:
            mi=tot
        if ma<tot:
            ma=tot   
dfs(0,oper,s[0])
print(ma)
print(mi)





