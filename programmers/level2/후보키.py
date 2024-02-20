def is_unique(keys, relation):
    tmp = set()
    for r in relation:
        tp = []
        for key in keys:
            tp.append(r[key])
        tmp.add(tuple(tp))
    return len(relation) == len(tmp)
    
def remove_dupl(answer):
    for i in range(len(answer)):
        answer[i] = set(answer[i])
    real = 0
    print(answer)
    for i in range(len(answer)):
        is_ok = 0
        for j in range(len(answer)):
            if answer[j].issubset(answer[i]):
                is_ok += 1
        if is_ok == 1:
            real += 1
    return real
            
def solution(relation):
    global row, col, answer
    row = len(relation)
    col = len(relation[0])
    answer = []
    
    def dfs(keys, max_key, now):
        global row, col, answer
        if len(keys) == max_key:
            return
        if is_unique(keys, relation):
            print(keys)
            answer.append(keys[:])
            return
        else:
            for i in range(now + 1, col):
                keys.append(i)
                dfs(keys, max_key, i)
                keys.pop()
            
    dfs([], row, -1)
    return remove_dupl(answer)
