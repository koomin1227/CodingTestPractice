#https://www.acmicpc.net/problem/2473
from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
def minimum(mini,a,f,r,sum1):
    if mini[0]>a:
        mini[0]=a
        mini[1]=f
        mini[2]=r
        mini[3]=sum1
    return mini
#투포인터


ans=[3000000000,0,0,0]
for i in range(n):
    r=0
    f=n-1
    if r==i:
        r+=1
    elif f==i:
        f-=1
    mini=[3000000000,f,r,0]
    target=0-arr[i]
    while True:
        cur_sum=arr[r]+arr[f]
        cur_sub=abs(cur_sum-target)
        mini=minimum(mini,cur_sub,f,r,cur_sum)
        if cur_sum<target:
            r=r+1
            if r==i:
                r+=1
        else:
            f=f-1
            if f==i:
                f-=1
        if r==f:
            break
    ans=minimum(ans,abs(mini[3]+arr[i]),mini[2],mini[1],i)

res=[arr[ans[1]], arr[ans[2]],arr[ans[3]]]
res.sort()    
for i in res:
    print(i,end=' ')
# print(ans)