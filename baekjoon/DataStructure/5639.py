#https://www.acmicpc.net/problem/5639
#두번째 시도 (성공)
import sys 
from collections import deque
from itertools import product
import copy
import heapq
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
num_list = []
#입력
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break
#전위순회 자체에서 후위 순회를 실시한다
def post_search(start,end):
    if start>=end:
        return 
    root=num_list[start]
    #오른쪽 노드가 존재하지 않는 경우
    if num_list[end-1]<=root:
        post_search(start+1,end)
        print(root)
        return
    tmp=0
    for i in range(start+1,end+1):
        if root<num_list[i]:
            tmp=i
            break

    post_search(start+1,tmp)
    post_search(tmp,end)
    print(root)
post_search(0,len(num_list))
