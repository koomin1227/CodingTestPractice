from sys import stdin
input=stdin.readline
n = int(input())
nums = list(map(int, input().split()))

sums = []
temp = 0
ans = 0
i = 0
j = n - 1
while i + 1 < j:
    now = min(nums[i], nums[j]) * (j -i -1)
    ans = max(ans, now)
    if nums[i] < nums[j]:
        i += 1
    else:
        j -= 1
print(ans)