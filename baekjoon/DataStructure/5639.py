#https://www.acmicpc.net/problem/5639
#첫번째 시도 실패 (시간초과)
import sys 
from collections import deque
from itertools import product
import copy
import heapq
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append([num,0])
    except:
        break
tree={}
for i in range(len(num_list)):
    left=0
    right=0
    for j in range(i+1,len(num_list)):
        if num_list[j][1]==1:
            break
        if left==0 and num_list[j][0]<num_list[i][0]:
            left=num_list[j][0]
            num_list[j][1]=1
        elif right==0 and num_list[j][0]>num_list[i][0]:
            right=num_list[j][0]
            num_list[j][1]=1
    tree[num_list[i][0]]=[left,right]
def post_search(node):
    if node==0:
        return 
    post_search(tree[node][0])
    post_search(tree[node][1])
    print(node)
post_search(num_list[0][0])
