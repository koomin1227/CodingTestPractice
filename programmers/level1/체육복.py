def solution(n, lost, reserve):
    lost_s = list(set(lost) - set(reserve))
    reserve_s = list(set(reserve) - set(lost))
    for i in reserve_s:
        prev = i - 1
        nex = i + 1
        if prev in lost_s:
            lost_s.remove(prev)
        elif nex in lost_s:
            lost_s.remove(nex)    
    answer = n - len(lost_s)
    return answer