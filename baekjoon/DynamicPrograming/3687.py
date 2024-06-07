def find_max(n):
    dic = {2:1, 3:7, 4: 4, 5:5, 6:9, 7:8 }
    ans = []
    while n != 0:
        if n - 2 > 1:
            ans.append(dic[2])
            n = n - 2
        else:
            ans.append(dic[n])
            n = n - n
    ans.reverse()
    res = 0
    for i in ans:
        res = res * 10 + i
    return res

def find_min(n):
    dic = {2:1, 3:7, 4: 4, 5:2, 6:0, 7:8 }
    dp = [0,0,1,7,4,2,6,8] + ([0] * 100)
    for i in range(8, n + 1):
        tmp = []
        for j in range(2, 8):
            if i - j >= 2:
                tmp.append(dp[i-j] * 10 + dic[j])
        dp[i] = min(tmp)
    return dp[n]


t = int(input())
nums = []
for _ in range(t):
    nums.append(int(input()))
for num in nums:
    print(find_min(num), find_max(num))


