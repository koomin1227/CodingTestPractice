from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
k = int(input())
planet_map = []
for _ in range(m):
    planet_map.append(list(input()))
inspects = []
for _ in range(k):
    inspects.append(list(map(int,input().split())))

ice_prefix_sum = [[0] * n for _ in range(m)]
ocean_prefix_sum = [[0] * n for _ in range(m)]
jungle_prefix_sum = [[0] * n for _ in range(m)]
prefix_sums = [jungle_prefix_sum, ocean_prefix_sum, ice_prefix_sum]
sections = ['J', 'O', 'I']
for h in range(3):
    section = sections[h]
    prefix_sum = prefix_sums[h]
    for i in range(m):
        for j in range(n):
            value = 0
            if planet_map[i][j] == section:
                value = 1
            if i == 0 and j == 0:
                prefix_sum[i][j] = value
            elif i == 0:
                prefix_sum[i][j] = prefix_sum[i][j - 1] + value
            elif j == 0:
                prefix_sum[i][j] = prefix_sum[i - 1][j] + value
            else:
                prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + value

for h in range(k):
    ans = []
    a1, b1, a2, b2 = inspects[h]
    a1, b1, a2, b2 = a1-1, b1-1, a2-1, b2-1 
    for e in range(3):
        total = 0
        prefix_sum = prefix_sums[e]
        if a1  - 1 < 0 and b1  - 1 < 0:
            total = prefix_sums[e][a2][b2]
        elif a1  - 1 < 0:
            total = prefix_sums[e][a2][b2] - prefix_sums[e][a2][b1 - 1]
        elif b1  - 1 < 0:
            total = prefix_sums[e][a2][b2] - prefix_sums[e][a1 - 1][b2]
        else:
            total = prefix_sums[e][a2][b2] - prefix_sums[e][a1 - 1][b2] - prefix_sums[e][a2][b1 - 1] + prefix_sums[e][a1 - 1][b1 - 1]
        ans.append(total)
    print(ans[0], ans[1], ans[2])