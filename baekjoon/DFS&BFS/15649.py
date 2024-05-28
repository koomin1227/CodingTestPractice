n, m = map(int,input().split())
def dfs(depth, nums):
  if depth == m:
    for i in nums:
      print(i,end=' ')
    print()
    return
  for i in range(1, n + 1):
    if i not in nums: 
        nums.append(i)
        dfs(depth + 1, nums)
        nums.pop()
dfs(0, [])