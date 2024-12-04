from sys import stdin
input=stdin.readline

answer = 0
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()

for i in range(n):
    if nums[i] > 0:
        break

n_nums = nums[0:i]
p_nums = nums[i:]

i = len(p_nums) - 1
while i >= 0:
    if i >= 1:
        now = p_nums[i]
        prev = p_nums[i - 1]
        if now * prev > now + prev:
            answer += now * prev
        else:
            answer += now + prev
        i -= 2
    else:
        answer += p_nums[i]
        i -= 1

i = 0
while i < len(n_nums):
    if i < len(n_nums) - 1:
        now = n_nums[i]
        next = n_nums[i + 1]
        if now * next > now + next:
            answer += now * next
        else:
            answer += now + next
        i += 2
    else:
        answer += n_nums[i]
        i += 1
print(answer)
