#https://www.acmicpc.net/problem/2166
from sys import stdin
input=stdin.readline

n=int(input())
coordinate=[]
for i in range(n):
    coordinate.append(list(map(int,input().split())))
coordinate.append(coordinate[0])
xSum=0
ySum=0
for i in range(n):
    xSum+=coordinate[i][0]*coordinate[i+1][1]
    ySum+=coordinate[i][1]*coordinate[i+1][0]
area=abs(xSum-ySum)/2

print(round(abs(xSum-ySum)/2,1))
