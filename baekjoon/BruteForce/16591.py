n, k = map(int, input().split())
arr = list(map(int,input().split()))

ans = 1001

for i in range(n):
    if arr[i] - (i * k) < 1:
        continue
    cnt = 0
    for j in range(n):
        if j < i and arr[j] != arr[i] - ((i - j) *k):
            cnt += 1
        elif j > i and arr[j] != arr[i] + ((j - i) *k):
            cnt += 1
    ans = min(ans, cnt)
print(ans)
