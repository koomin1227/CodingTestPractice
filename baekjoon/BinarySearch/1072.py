#https://www.acmicpc.net/problem/1072

#방정식 이용 버전
# import math
# x,y=map(int,input().split())
# if x==0:
#     z=0
# else:
#     z=int((y*100/x))
# b=z+1
# if z>=99:
#     print(-1)
# else:
#     a=(b*x-100*y)/(100-b)
#     if x==0:
#         a=1
#     print(math.ceil(a))

# 이분 탐색 이용 버전
from sys import stdin
input=stdin.readline
x,y=map(int,input().split())
if x==0:
    z=0
else:
    z=int((y*100/x))
if z>=99:
    print(-1)
elif x==0:
    print(1)
else:
    left=0
    right=1000000000
    while left<=right:
        mid=(left+right)//2
        res=int(((y+mid)*100/(x+mid)))
        if res>z:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    print(ans)