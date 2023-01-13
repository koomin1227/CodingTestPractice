#https://www.acmicpc.net/problem/2166
from sys import stdin
input=stdin.readline
n=int(input())
cod=[]
for i in range(n):
    cod.append(list(map(int,input().split())))
cod.append(cod[0])
xSum,ySum=0,0
area=0
for i in range(n):
    area+=cod[i][0]*cod[i+1][1]-cod[i][1]*cod[i+1][0]
print(round(abs(area)/2,1))
