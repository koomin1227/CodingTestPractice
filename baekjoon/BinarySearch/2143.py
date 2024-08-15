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
accum_a = [0]
accum_b = [0]

tot = 0
for i in range(n):
    tot += a[i]
    accum_a.append(tot)
for i in range(1, n + 1):
    for j in range(i,n + 1):
        A.append(accum_a[j] - accum_a[i - 1])

tot = 0
for i in range(m):
    tot += b[i]
    accum_b.append(tot)

for i in range(1, m + 1):
    for j in range(i,m + 1):
        B.append(accum_b[j] - accum_b[i-1])
B.sort()
answer = 0
for i in A:
    target = t - i
    l = binary_search_left(target, B)
    if l != -1:
        r = binary_search_right(target, B)
        answer += (r - l + 1)


print(answer)