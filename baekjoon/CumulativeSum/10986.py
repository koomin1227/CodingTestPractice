from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

remainder = [0] * m
total = 0
for i in range(n):
    total += nums[i]
    remainder[total % m] += 1

answer = remainder[0]
for i in range(m):
    answer += (remainder[i] * (remainder[i] - 1)) // 2

print(answer)