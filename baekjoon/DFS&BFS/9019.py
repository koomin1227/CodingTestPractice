from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline

def oper(n,num):
    if n==0:
        return (num*2)%10000
    elif n==1:
        if num==0:
            return 9999
        else:
            return num-1
    elif n==2:
        return (num%1000)*10+num//1000
    elif n==3:
        return num//10+(num%10)*1000

t=int(input())
do=['D','S','L','R']

for _ in range(t):
    a,b=map(int,input().split())
    visited=[0]*10000
    que=deque()
    que.append([a,''])
    tmp=False
    while que:
        x,o=que.popleft()
        for i in range(4):
            nx=oper(i,x)
            no=o+do[i]
            if visited[nx]==1:
                continue
            if nx==b:
                print(no)
                tmp=True
                break
            visited[nx]=1
            que.append([nx,no])
        if tmp:
            break
