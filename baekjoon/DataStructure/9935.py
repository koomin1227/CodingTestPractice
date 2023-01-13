#https://www.acmicpc.net/problem/9935
from sys import stdin
from collections import deque
from itertools import combinations
import copy
import heapq
input=stdin.readline
st=input().rstrip()
boom=input().rstrip()
boom_len=len(boom)
boom_last=boom[-1]
nst=[]
cnt=0
for i in range(len(st)):
    nst.append(st[i])
    if st[i]==boom_last and i>=boom_len-1 and len(nst)>=boom_len:
        cnt=0
        for j in range(boom_len):
            if nst[-1-j]==boom[boom_len-j-1]:
                cnt+=1
        if cnt==boom_len:
            for _ in range(boom_len):
                nst.pop()

if len(nst)==0:
    print('FRULA')
else:       
    for i in range(len(nst)):
        print(nst[i],end='')



