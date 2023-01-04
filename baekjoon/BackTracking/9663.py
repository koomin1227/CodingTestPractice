#https://www.acmicpc.net/problem/9663
n=int(input())
row=[0]*n#퀸의 자리를 담을 리스트
tot=0

def check(x):#x번째 줄의 퀸이 맞는 자리인지 검사
    for i in range(x):
        if row[i]==row[x] or abs(i-x)==abs(row[i]-row[x]):
            return False
    return True

def dfs(x):#dfs로 퀸의 자리 탐색
    global tot
    if x==n:
        tot+=1
        return
    for i in range(n):#x번째 줄에서 0~n-1 까지 탐색
        row[x]=i#일단 x번째 줄 i번째에 퀸을 놔본다
        if check(x)==True:#유호한 자리이면 다음 줄로 넘어감
            dfs(x+1)

dfs(0)
print(tot)

