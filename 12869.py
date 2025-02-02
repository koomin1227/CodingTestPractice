n = int(input())
scvs = list(map(int, input().split()))
scvs.extend([0, 0])

combs = [(9,3,1),(9,1,3),(3,9,1),(3,1,9),(1,3,9),(1,9,3)]
dp = [[[0]*61 for _ in range(61)] for _ in range(61)]
dp[scvs[0]][scvs[1]][scvs[2]] = 1
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for comb in combs:
                    ni = i - comb[0] if i - comb[0] >= 0 else 0
                    nj = j - comb[1] if j - comb[1] >= 0 else 0
                    nk = k - comb[2] if k - comb[2] >= 0 else 0
                    if dp[ni][nj][nk] == 0 or dp[ni][nj][nk] > dp[i][j][k] + 1:
                        dp[ni][nj][nk] = dp[i][j][k] + 1
print(dp[0][0][0] - 1)
