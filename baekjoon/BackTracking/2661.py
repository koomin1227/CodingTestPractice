n = int(input())

def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True
    
def dfs(nums, n):
    if len(nums) == n:
        print(nums)
        exit()
    for i in range(1,4):
        if check(nums + str(i)):
            dfs(nums + str(i), n)

dfs('', n)