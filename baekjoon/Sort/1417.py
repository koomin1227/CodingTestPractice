n = input()
nums = []
for i in range(len(n)):
    nums.append(n[i])
nums.sort(reverse=True)

for i in nums:
    print(i,end='')
# print(nums)