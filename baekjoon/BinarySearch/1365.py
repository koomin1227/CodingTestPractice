n = int(input())
nums = list(map(int,input().split()))

def binary_search(target, dp):
    start = 0
    end = len(dp) - 1
    while start < end:
        mid = (start + end) // 2
        if dp[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end
    

dp = []
dp.append(nums[0])

for i in range(1, n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
        
    else:
        index = binary_search(nums[i], dp)
        dp[index] = nums[i]
print(n - len(dp))