#https://www.acmicpc.net/problem/9663
n=int(input())
row=[0]*n
tot=0

def check(x):
    for i in range(x):
        if row[i]==row[x] or abs(i-x)==abs(row[i]-row[x]):
            return False
    return True
def dfs(x):
    global tot
    if x==n:
        tot+=1
        return
    for i in range(n):
        row[x]=i
        if check(x)==True:
            dfs(x+1)

dfs(0)
print(tot)
