n = int(input())
series = list(map(int,input().split()))

dp_up = [1]*n
dp_down = [1]*n

for i in range(n):
    for j in range(i):
        if series[i]>series[j]:
            dp_up[i] = max(dp_up[i],dp_up[j] + 1)
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if series[i]>series[j]:
            dp_down[i] = max(dp_down[i],dp_down[j] + 1)
max_len = max(max(dp_down),max(dp_up))
for i in range(0,n):
    tmp_up = dp_up[i]
    tmp_down = 0
    for j in range(i+1,n):
        if series[i]>series[j]:
            tmp_down = max(tmp_down,dp_down[j])
    max_len = max(max_len,tmp_up+tmp_down)

print(max_len)