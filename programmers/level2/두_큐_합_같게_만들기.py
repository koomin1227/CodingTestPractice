from collections import deque
def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    max_len = len(queue1) * 3
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    
    while True:
        if answer > max_len:
            return -1
        if sum2 > sum1:
            tmp = queue2.popleft()
            sum2 -= tmp
            sum1 += tmp
            queue1.append(tmp)
            answer += 1
        elif sum2 < sum1:
            tmp = queue1.popleft()
            sum1 -= tmp
            sum2 += tmp
            queue2.append(tmp)
            answer += 1
        else:
            break
    return answer