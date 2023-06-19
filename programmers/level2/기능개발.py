def solution(progresses, speeds):
    answer = []
    start = 0
    for i in range(101):
        if start == len(progresses):
            break
        cnt = 0
        for j in range(start, len(progresses)):
            if progresses[j] < 100: 
                progresses[j] += speeds[j]
        if progresses[start] >= 100:
            for j in range(start, len(progresses)):
                if progresses[j] < 100: break
                cnt +=1
                start += 1
            answer.append(cnt)
    return answer