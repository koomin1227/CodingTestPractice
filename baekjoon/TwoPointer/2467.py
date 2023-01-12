#https://www.acmicpc.net/problem/2467
from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))

def minimum(mini,a,f,r):
    if mini[0]>a:
        mini[0]=a
        mini[1]=f
        mini[2]=r
    return mini
#투포인터
r=0
f=n-1
mini=[abs(arr[r]+arr[f]),f,r]

while True:
    if r+1==f:
        break
    if abs(arr[r+1]+arr[f])<abs(arr[r]+arr[f-1]):
        mini=minimum(mini,abs(arr[r+1]+arr[f]),f,r+1)
        r=r+1
    else:
        mini=minimum(mini,abs(arr[r]+arr[f-1]),f-1,r)
        f=f-1
    
print(arr[mini[2]], arr[mini[1]])