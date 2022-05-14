from sys import stdin
import copy
#+,-,,*,/

n=int(stdin.readline())
s=list(map(int,stdin.readline().split()))
oper=list(map(int,stdin.readline().split()))
mi=1000000001
ma=-1000000001
def dfs(x,oper,tot):
    for i in range(4):
        n_oper=copy.deepcopy(oper)
        if n_oper[i]!=0:
            n_oper[i]-=1
            dfs(x+1,n_oper,cal(tot,s[x+1],i))
    if (x==n-1):
        global mi
        global ma
        if mi>tot:
            mi=tot
        if ma<tot:
            ma=tot
            
        

def cal(a,b,o):
    t=0
    if o==0:
        t=a+b
    elif o==1:
        t=a-b
    elif o==2:
        t=a*b
    elif o==3:
        if a>=0:
            t=a//b
        else:
            a*=-1
            t=a//b
            t*=-1
    return t
        

dfs(0,oper,s[0])
print(ma)
print(mi)





