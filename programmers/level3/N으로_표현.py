def solution(N, number):
    def make_NN(n):
        res = 0
        for i in range(n):
            res = res*10 + N
        return res
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1,9):
        dp[i].append(make_NN(i))
        for j in range(1,i):
            NN = make_NN(i-j)
            for prev_num in dp[j]:
                dp[i].append(prev_num + NN)
                dp[i].append(prev_num - NN)
                dp[i].append(prev_num * NN)
                dp[i].append(prev_num / NN)
                dp[i].append((-1)*prev_num + NN)
        if number in dp[i]:
            answer = i
            break
    return answer
print(solution(6,5))