from sys import stdin
input = stdin.readline

n = int(input())
nums = [[0, 'A', -1], [0, 'B', -1], [0, 'C', -1], [0, 'D', -1], [0, 'E', -1]
        , [0, 'F', -1], [0, 'G', -1], [0, 'H', -1], [0, 'I', -1], [0, 'J', -1]]
not_zero = set()
for i in range(n):
    alpa = input()
    not_zero.add(alpa[0])
    for j in range(len(alpa) - 1):
        d = (len(alpa) - 1) - (j + 1)
        nums[ord(alpa[j]) - ord('A')][0] += 10 ** d
nums.sort()
if nums[0][0] != 0:
    for i in range(10):
        cur = nums[i]
        if cur[1] in not_zero:
            continue
        else:
            cur[2] = 0
            break
ans = 0
num = 9
for i in range(9, -1, -1):
    cur = nums[i]
    if cur[2] == 0:
        continue
    if cur[0] == 0:
        break
    ans += cur[0] * num
    num -= 1
print(ans)

