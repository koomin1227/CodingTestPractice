from sys import stdin
input = stdin.readline

n = int(input())
buildings = list(map(int, input().split()))

def is_visible(x1, x2, a, b):
    if x1 < x2:
        start, end = x1, x2
    else:
        start, end = x2, x1
    for i in range(start + 1, end):
        y = a * i + b
        if y <= buildings[i]:
            return False
    return True

answer = 0
for i in range(n):
    cnt = 0
    x1, y1 = i, buildings[i]
    for j in range(n):
        if i == j:
            continue
        x2, y2 = j, buildings[j]
        a = (y2 - y1) / (x2 - x1)
        b = y1 - (a * x1)
        if is_visible(x1, x2, a, b):
            cnt += 1
    answer = max(answer, cnt)
print(answer)