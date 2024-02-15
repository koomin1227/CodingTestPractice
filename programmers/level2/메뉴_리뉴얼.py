## 처음 생각대로 푼 버전
from itertools import combinations
def solution(orders, course):
    answer = []
    len_cnt = [[] for _ in range(11)]
    
    for order in orders:
        tmp = list(order)
        tmp.sort()
        for c in course:
            len_cnt[c] += list(combinations(tmp, c))
    
    for c in course:
        len_cnt[c].sort()
        target = len_cnt[c]
        
        max_cnt = 0
        i,j = 0,0
        while True:
            if j == len(target):
                max_cnt = max(j - i, max_cnt)
                break
            if target[i] == target[j]:
                j += 1
            elif target[i] != target[j]:
                max_cnt = max(j - i, max_cnt)
                i += 1
                
        if max_cnt > 1:
            i,j = 0,0
            while True:
                if j == len(target):
                    if i != j and (j - i) == max_cnt:
                        answer.append(''.join(target[i]))
                    break
                if target[i] == target[j]:
                    j += 1
                elif target[i] != target[j]:
                    if (j - i) == max_cnt:
                        answer.append(''.join(target[i]))
                    i += 1

    answer.sort()        
    return answer


## dict 사용 버전 이게 더 빠름
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    len_cnt = [defaultdict(int) for _ in range(11)]
    for order in orders:
        tmp = list(order)
        tmp.sort()
        for c in course:
            for comb in combinations(tmp, c):
                len_cnt[c][''.join(comb)] += 1

    for c in course:
        menus = len_cnt[c]
        res= []
        for menu in menus:
            res.append([menus[menu], menu])
        res.sort(reverse = True)
        for re in res:
            if res[0][0] == 1 or re[0] != res[0][0]:
                break
            answer.append(re[1])
    answer.sort()    
    return answer