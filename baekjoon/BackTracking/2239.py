#https://www.acmicpc.net/problem/2239
sdoku=[]
arr=[]
for i in range(9):
    sdoku.append(list(input().strip()))
    for j in range(9):
        if sdoku[i][j]=='0':
            arr.append([i,j])

def solve(n):
    if n==len(arr):
        for i in range(9):
            for j in range(9):
                print(int(sdoku[i][j]),end='')
            print()
        return 0
    row,col=arr[n]
    nums=[1,2,3,4,5,6,7,8,9]
    for r in range(9):
        if int(sdoku[r][col]) in nums:
            nums.remove(int(sdoku[r][col]))
    for c in range(9):
        if int(sdoku[row][c]) in nums:
            nums.remove(int(sdoku[row][c]))
    for r in range((row//3)*3,(row//3)*3+3):
        for c in range((col//3)*3,(col//3)*3+3):
            if int(sdoku[r][c]) in nums:
                nums.remove(int(sdoku[r][c]))
    for i in nums:
        sdoku[row][col]=i
        if solve(n+1)==0:
            return 0
    sdoku[row][col]=0
solve(0)               
