from sys import stdin
input=stdin.readline

def binary_search_left(target,B):
    left = 0
    right = len(B) - 1
    while left<=right:
        mid = (left + right)//2
        if target == B[mid] and (mid == 0 or B[mid-1]<B[mid]):
            return mid
        elif target <= B[mid]:
            right = mid-1
        elif target>B[mid]:
            left = mid+1
    return -1

def binary_search_right(target,B):
    left = 0
    right = len(B) - 1
    while left<=right:
        mid = (left + right)//2
        if target == B[mid] and (mid == len(B) - 1 or B[mid+1]>B[mid]):
            return mid
        elif target < B[mid]:
            right = mid-1
        elif target>=B[mid]:
            left = mid+1
    return -1

t=int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
A = []
B = []
for i in range(n):
    for j in range(i,n):
        A.append(sum(a[i:j+1]))
for i in range(m):
    for j in range(i,m):
        B.append(sum(b[i:j+1]))
B.sort()
answer = 0
for i in A:
    target = t - i
    l = binary_search_left(target, B)
    if l != -1:
        r = binary_search_right(target, B)
        answer += (r - l + 1)


print(answer)