#https://www.acmicpc.net/problem/1647
from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
graph=[[]for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    graph[]