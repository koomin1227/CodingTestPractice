def solution(n, info):
    res = [0] * 11
    global max_dif, ans
    max_dif = 0
    ans = [-1]
    def dfs(n, s):
        global max_dif, ans
        if s == 11 or n == 0:
            a_score = 0
            l_score = 0
            for i in range(11):
                if res[i] > info[i]:
                    l_score += (10 - i)
                elif res[i] <= info[i] and info[i] != 0:
                    a_score += (10 - i)
            if l_score > a_score:
                if n >= 0:
                    res[10] = n
                if max_dif < l_score - a_score:
                    max_dif = l_score - a_score
                    ans = res.copy()
                elif max_dif == l_score - a_score:
                    is_win = False
                    for i in range(10, -1, -1):
                        if ans[i] < res[i]:
                            is_win = True
                            break
                        elif ans[i] > res[i]:
                            break
                    if is_win:
                        ans = res.copy()
            return
        if info[s] < n:
            res[s] = info[s] + 1
            dfs(n - (info[s] + 1), s+1)
            res[s] = 0
        dfs(n, s+1)
    dfs(n, 0)
    return ans

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]

print(solution(n, info))
