from sys import stdin
input = stdin.readline

n = int(input())
total = 0
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
    total += num
nums = nums * 2
s = 0
e = 1
sum = nums[0]
answer = 0
while s < n:
    other_sum = total - sum
    answer = max(answer, min(sum, other_sum))

    if sum >= (total // 2):
        sum -= nums[s]
        s += 1
    else:
        sum += nums[e]
        e += 1
        
print(answer)