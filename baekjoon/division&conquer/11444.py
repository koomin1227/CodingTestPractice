from sys import stdin
input = stdin.readline
n = int(input())

def mul(A,B):
    n = len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp = A[i][k]*B[k][j]
                C[i][j]+=tmp
                C[i][j] %= 1000000007
    return C

def dac(a,b):
    if b == 1:
        return a
    a_2 = dac(a,b//2)
    res = mul(a_2,a_2)
    if b%2 == 1:
        res = mul(res,a)
    return res

if n==0:
    print(0)
else:
    a = [[1,1],[1,0]]
    res = dac(a,n)
    print(res[0][1])

