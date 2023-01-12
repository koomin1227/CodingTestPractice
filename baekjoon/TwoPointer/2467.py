#https://www.acmicpc.net/problem/2473
from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
def minimum(mini,a,f,r):
    if mini[0]>a:
        mini[0]=a
        mini[1]=f
        mini[2]=r
    return mini
#투포인터
r=0
f=n-1
mini=[3000000000,f,r]

while True:
    cur_sum=arr[r]+arr[f]
    mini=minimum(mini,abs(cur_sum),f,r)
    if cur_sum<0:
        r=r+1
    else:
        f=f-1
    if r==f:
        break
    
print(arr[mini[2]], arr[mini[1]])