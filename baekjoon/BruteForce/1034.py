n,m = map(int, input().split())

table = []
for i in range(n):
    table.append(list(input()))
k = int(input())

dic = {}

for row in table:
    zero_cnt = 0
    for c in row:
        if c == '0':
            zero_cnt += 1

    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        if tuple(row) not in dic:
            dic[tuple(row)] = 0
        dic[tuple(row)] += 1
answer = 0
for key in dic.keys():
    answer = max(answer, dic[key])
print(answer)

    