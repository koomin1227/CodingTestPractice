def solution(n, results):
    answer = 0
    INF=int(1e9)
    table = [[None] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        table[i][i] = 0
    for result in results:
        a, b = result
        table[a][b] = 1
        table[b][a] = -1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if table[a][k] == table[k][b] and (table[k][b] == 1 or table[k][b] == -1):
                    table[a][b] = table[a][k]

    for a in range(1, n + 1):
        is_sure = True
        for b in range(1, n + 1):
            if table[a][b] == None:
                is_sure = False
                break
        if is_sure:
            answer += 1

    return answer