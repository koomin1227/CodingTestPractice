#https://www.acmicpc.net/problem/1806
from sys import stdin
input=stdin.readline

n,s=map(int,input().split())
pro=list(map(int,input().split()))
f,r=0,0
min_len=n+1
tot=pro[0]
#간략한 버전
while True:
    if tot>=s:
        tot-=pro[r]
        min_len=min(min_len,f-r+1)
        r+=1
    else:
        f+=1
        if f==n:
            break
        tot+=pro[f]
#혼자 짜본 투포인터 버전
# while r<n:
#     if f<n-1:
#         if tot>=s:
#             min_len=min(min_len,f-r+1)
#             if f==r:
#                 f+=1
#                 tot+=pro[f]
#             else:
#                 tot-=pro[r]
#                 r+=1
#         elif tot<s:
#             f+=1
#             tot+=pro[f]  
#     else:
#         if tot>=s:
#             min_len=min(min_len,f-r+1)
#         tot-=pro[r]
#         r+=1
if min_len==n+1:
    print(0)
else:
    print(min_len)
#골드문제
