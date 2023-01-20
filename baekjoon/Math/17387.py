#https://www.acmicpc.net/problem/17387
from sys import stdin
input=stdin.readline
def CCW(x1,y1,x2,y2,x3,y3):
    tmp=x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)
    if abs(tmp)-0.000001==0:
        return 0
    elif tmp==0:
        return 0
    elif tmp<0:
        return -1
    else:
        return 1
#ccw 음수: 시계방향, 양수: 반시계 방향, 0: 평행
x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())
ccw123=CCW(x1,y1,x2,y2,x3,y3)
ccw124=CCW(x1,y1,x2,y2,x4,y4)
ccw134=CCW(x1,y1,x3,y3,x4,y4)
ccw234=CCW(x2,y2,x3,y3,x4,y4)

ans=0
mx1,mx2=min(x1,x2),max(x1,x2)
mx3,mx4=min(x3,x4),max(x3,x4)
my1,my2=min(y1,y2),max(y1,y2)
my3,my4=min(y3,y4),max(y3,y4)
if ccw123*ccw124==0 and ccw134*ccw234==0:
    if (mx3<=mx2 and mx1<=mx4) and (my3<=my2 and my1<=my4):
        ans=1
elif ccw123*ccw124<=0 and ccw134*ccw234<=0:
    ans=1
print(ans)



