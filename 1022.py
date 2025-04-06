r1, c1, r2, c2 = map(int, input().split())

x = r2 - r1 + 1
y = c2 - c1 + 1

arr = [[0] * y for _ in range(x)]
max_len = 0
for i in range(x):
    for j in range(y):
        r = i + r1
        c = j + c1
        if abs(r) == abs(c):
            if r > 0 and c > 0:
                arr[i][j] = 4 * (r ** 2) + 4 * r + 1
            elif r > 0 and c < 0:
                arr[i][j] = 4 * (r ** 2) + 2 * r + 1
            elif r < 0 and c < 0:
                arr[i][j] = 4 * (abs(r) ** 2) + 1
            elif r < 0 and c > 0:
                arr[i][j] = 4 * (abs(r) ** 2) -2 * abs(r) + 1
            elif r == 0 and c == 0:
                arr[i][j] = 1
        else:
            if r < 0 and abs(r) > abs(c):
                arr[i][j] = 4 * (abs(r) ** 2) + 1 - (c - r)
            elif c < 0 and abs(r) < abs(c):
                arr[i][j] = 4 * (abs(c) ** 2) + 1 + (r - c)
            elif r > 0 and abs(r) > abs(c):
                arr[i][j] = 4 * (r ** 2) + 4 * r + 1 - (r - c)
            elif c > 0 and abs(r) < abs(c):
                arr[i][j] = 4 * (c ** 2) - 2 * c + 1  (c + r)
        max_len = max(len(str(arr[i][j])), max_len)

for i in range(x):
    for j in range(y):
        if len(str(arr[i][j])) < max_len:
            # max_len 길이만큼 오른쪽에 공백을 채운다.
            print(str(arr[i][j]).rjust(max_len,' '), end=' ')
        else:
            print(arr[i][j], end=' ')
    print()