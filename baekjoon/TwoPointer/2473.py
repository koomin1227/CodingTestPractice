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
for i in range(n-2):
    r=i+1
    f=n-1
    while r<f:
        cur_sum=arr[r]+arr[f]+arr[i]
        ans=minimum(ans,abs(cur_sum),f,r,i)
        if cur_sum<0:
            r=r+1
        else:
            f=f-1

res=[arr[ans[1]], arr[ans[2]],arr[ans[3]]]
res.sort()    
for i in res:
    print(i,end=' ')
