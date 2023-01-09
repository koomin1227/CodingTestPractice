#https://www.acmicpc.net/problem/1208
from sys import stdin
from itertools import combinations
input=stdin.readline
n,s=map(int,input().split())
arr=list(map(int,input().split()))
tot=0
# 1. 수열을 반으로 쪼갠다
front=arr[:n//2]
rear=arr[(n//2):]
# 2. 두 수열의 부분 합으 구한다.
fSum=[]
for i in range(1,len(front)+1):
    for j in combinations(front,i):
        tmp=sum(j)
        if tmp==s:
            tot+=1
        fSum.append(tmp)
# print(fSum)
rSum=[]
for i in range(1,len(rear)+1):
    for j in combinations(rear,i):
        tmp=sum(j)
        if tmp==s:
            tot+=1
        rSum.append(tmp)
# print(rSum)
# 3. rear 수열을 정렬
rSum.sort()
# 4. fSum을 훑으며 sum-fSum[i] 인 값을 rSum에서 이진 탐색으로 찾는다.
for i in fSum:
    target=s-i
    left=0
    right=len(rSum)-1
    lans=-1
    while left<=right:
        mid=(left+right)//2
        if rSum[mid]==target and (mid==0 or rSum[mid-1]<target):
            lans=mid
            break
        elif rSum[mid]<target:
            left=mid+1
        elif rSum[mid]>=target:
            right=mid-1
            
    if lans!=-1:
        left=lans
        right=len(rSum)-1
        rans=-1
        while left<=right:
            mid=(left+right)//2
            if rSum[mid]==target and (mid==len(rSum)-1 or rSum[mid+1]>target):
                rans=mid
                break
            elif rSum[mid]<=target:
                left=mid+1
            elif rSum[mid]>target:
                right=mid-1
        if rans!=-1:
            tot+=(rans-lans)+1
print(tot)        

# print(front)
# print(rear)



