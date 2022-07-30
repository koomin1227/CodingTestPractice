from sys import stdin

n=int(stdin.readline())
school=[]
teacher=[]
for i in range(n):
    tmp=list(map(str,stdin.readline().rstrip().split()))
    for j in range(n):
        if tmp[j]=='T':
            teacher.append([i,j])
    school.append(tmp)
def check(tx,ty):
    check=False
    for i in range(ty-1,-1,-1):
        if school[tx][i]=='O':
            break
        if school[tx][i]=='S':
            check=True
    for i in range(ty+1,n):
        if school[tx][i]=='O':
            break
        if school[tx][i]=='S':
            check=True
    for i in range(tx-1,-1,-1):
        if school[i][ty]=='O':
            break
        if school[i][ty]=='S':
            check=True
    for i in range(tx+1,n):
        if school[i][ty]=='O':
            break
        if school[i][ty]=='S':
            check=True
    return check
count=0
tmp=False
def dfs(count):
    global tmp
    if count==3:
        ccount=0
        for k in teacher:
            if check(k[0],k[1])==False:
                ccount+=1
            
        if ccount==len(teacher):
            tmp=True
        return
    for i in range(n):
        for j in range(n):
            if school[i][j]=='X':
                school[i][j]='O'
                count+=1
                dfs(count)
                count-=1
                school[i][j]='X'
dfs(count)
if tmp==True:
    print('YES')
else:
    print('NO')


"""
5
X S O X T
T X S X X
X X X X X
X T X X X
X X T X X

4
X S X T
X X S X
X X X X
T T T X

5
X X S X X
X X X X X
S X T X S
X X X X X
X X S X X

5
X T X T X
T X S X T
X S S S X
T X S X X
X T X X X

5
X S S S X
T X X S X
X T X S X
X X T X S
X X X T X

반례
3
X X S
X X X
T X X
NO
"""
