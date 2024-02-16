def binary_search(lst, target):
    l = 0
    r = len(lst)
    while l < r:
        mid = (l + r) // 2
        if lst[mid] >= target:
                r = mid
        else:
            l = mid + 1
    return len(lst) - l
            
def solution(info, query):
    answer = []
    language = ['cpp', 'java', 'python', '-']
    position = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']
    dic = dict()
    for l in language:
        for p in position:
            for c in career:
                for f in food:
                    dic.setdefault((l,p,c,f), list())
    
    for i in info:
        l1,p1,c1,f1,s = i.split(' ')
        for l in [l1, '-']:
            for p in [p1, '-']:
                for c in [c1, '-']:
                    for f in [f1, '-']:
                        dic[(l,p,c,f)].append(int(s))
    for d in dic:
        dic[d].sort()
        
    for q in query:
        l,p,c,tmp = q.split(' and ')
        f,s = tmp.split(' ')
        target = dic[(l,p,c,f)]
        cnt = binary_search(target, int(s))
        answer.append(cnt)


    return answer
