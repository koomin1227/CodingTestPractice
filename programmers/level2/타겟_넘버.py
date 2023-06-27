def solution(numbers, target):
    global answer
    answer = 0
    len_n = len(numbers)
    def dfs(depth,tot):
        global answer
        if depth == len_n:
            if tot == target:
                answer +=1
            return
        dfs(depth+1, tot + numbers[depth])
        dfs(depth + 1, tot - numbers[depth])
    dfs(0,0)
    return answer



    