N, M, H = map(int, input().split())
blocks = [[]]
for _ in range(N):
    blocks.append(list(map(int, input().split())))

dp = [[0] * (H + 1) for _ in range(N + 1)]

for student in range(1, N + 1):
    for h in range(H + 1):
        cur_blocks = blocks[student]
        dp[student][h] = dp[student - 1][h]
        for block_h in cur_blocks:
            if block_h == h:
                dp[student][h] += 1
            elif block_h > h:
                continue
            else:
                dp[student][h] += dp[student - 1][h - block_h]
        dp[student][h] = dp[student][h] % 10007
print(dp[N][H] % 10007)