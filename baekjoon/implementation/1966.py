t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    
    result = 1
    while que:
        if que[0] < max(que):
            que.append(que.pop(0))

        else:
            if m == 0: break

            que.pop(0)
            result += 1

        m = m - 1 if m > 0 else len(que) - 1

    print(result)
