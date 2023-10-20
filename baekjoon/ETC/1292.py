a,b = map(int,input().split())
nums = []

i = 1
for i in range(1,b+1):
  for j in range(i):
    nums.append(i)
    
print(sum(nums[a-1:b]))


