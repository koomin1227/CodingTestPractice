from sys import stdin
from collections import deque
import itertools 
import copy
import heapq
input=stdin.readline
def list_int(a):
    num=0
    for i in a:
        num=num*10+i
    return num
n=int(input())
m=int(input())
btn=[]
# 버튼 선별
if m!=0:
    l_btn=list(map(int,input().split()))
    for i in range(10):
        if i in l_btn:
            continue
        btn.append(i)
else:
    for i in range(10):
        btn.append(i)
#최솟값 찾기
mini=[100,abs(n-100)]
len=len(str(n))+1
#가능한 버튼의 조합을 완전탐색으로 탐색 그중 n과의 절댓값이 가장 작은 수 를 찾는다
for i in range(1,len+1):
    for j in itertools.product(btn,repeat=i):
        num=list_int(j)
        ab=abs(n-num)
        if mini[1]>i+ab:
            mini[0]=num
            mini[1]=i+ab
print(mini[1])
