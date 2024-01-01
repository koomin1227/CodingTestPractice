x, b = map(int, input().split())

ans = []
while x != 0:
    res = x % b
    x = x // b
    ans.append(res)
print(ans)

