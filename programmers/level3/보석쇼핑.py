from collections import deque
def solution(gems):
    answer = []
    kind = len(set(gems))
    if kind == 1:
        return [1,1]
    s,e = 0,0
    buy = {}
    buy[gems[0]] = 1
    min_section = len(gems) + 1
    
    while True:
        now_kind = len(buy)
        if now_kind == kind:
            if min_section > (e-s) + 1:
                min_section = (e-s) + 1
                answer = [s+1,e+1]
            buy[gems[s]] -= 1
            if buy[gems[s]] == 0:
                del buy[gems[s]]
            s += 1
            
        elif now_kind < kind:
            e += 1
            if e >= len(gems):
                break
            if gems[e] not in buy:
                buy[gems[e]] = 0
            buy[gems[e]] += 1
            
    return answer