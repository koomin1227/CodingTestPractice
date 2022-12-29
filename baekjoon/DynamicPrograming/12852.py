#https://www.acmicpc.net/problem/12852
n=int(input())
dp=[0 for _ in range(n+1)]
dp[1]=0
for i in range(2,n+1):
    a=i-1
    dp[i]=1+dp[a]
    if i%2==0:
        dp[i]=min(dp[i],1+dp[i//2])
    if i%3==0:
        dp[i]=min(dp[i],1+dp[i//3])
print(dp[n])
m=n
print(m,end=' ')
while m!=1:
    mini=dp[m]
    mininum=m
    if mini>dp[m-1]:
        mini=dp[m-1]
        mininum=m-1
    if m%2==0:
        if mini>dp[m//2]:
            mini=dp[m//2]
            mininum=m//2
    if m%3==0:
        if mini>dp[m//3]:
            mini=dp[m//3]
            mininum=m//3
    print(mininum,end=' ')
    m=mininum


