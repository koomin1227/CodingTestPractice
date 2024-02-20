def is_unique(keys, relation):
    tmp = set()
    for r in relation:
        tp = []
        for key in keys:
            tp.append(r[key])
        tmp.add(tuple(tp))
    return len(relation) == len(tmp)
    
    
    
def solution(relation):
    
    # print(is_unique([], relation))
    global row, col, answer
    row = len(relation)
    col = len(relation[0])
    answer = 0
    
    def dfs(keys, max_key, now):
        global row, col, answer
        if len(keys) == max_key:
            return
        if is_unique(keys, relation):
            answer += 1
            return
        else:
            for i in range(now + 1, col):
                keys.append(i)
                dfs(keys, max_key, i)
                keys.pop()
            
    dfs([], row, -1)
    return answer


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

res = solution(relation)

print(res)