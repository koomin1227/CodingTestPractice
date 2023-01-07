#https://www.acmicpc.net/problem/1072
import math
x,y=map(int,input().split())
if x==0:
    z=0
else:
    z=int((y*100/x))
b=z+1
if z>=99:
    print(-1)
else:
    a=(b*x-100*y)/(100-b)
    if x==0:
        a=1
    print(math.ceil(a))
# else:
#     cnt=0
#     newZ=z
#     while newZ==z: 
#         cnt+=1
#         newZ=int((y+cnt)/(x+cnt)*100)
    # print(cnt)
