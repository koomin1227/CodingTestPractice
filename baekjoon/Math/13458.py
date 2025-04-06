n = int(input())
examinees = list(map(int, input().split()))
b, c = map(int, input().split())

min_count = 0
for i in range(n):
    cur_examine = examinees[i]
    min_count += 1
    cur_examine -= b
    if cur_examine <= 0:
        continue
    min_count += cur_examine // c
    if cur_examine % c != 0:
        min_count += 1

print(min_count)