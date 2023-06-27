from sys import stdin
input = stdin.readline
def mul(A,B):
    n = len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp = A[i][k]*B[k][j]
                tmp = tmp % 1000
                C[i][j]+=tmp
    return C
def dac(a,b):
    if b == 1:
        return a
    
    a_2 = dac(a,b//2)
    res = mul(a_2,a_2)
    if b%2 == 1:
        res = mul(res,a)
    return res
n,b = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
res = dac(a,b)

for i in res:
    for j in i:
        print(j%1000,end=' ')
    print()
