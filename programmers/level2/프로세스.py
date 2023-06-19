from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque()
    for i in range(len(priorities)):
        que.append(i)
    while True:
        tmp = que.popleft()
        if max(priorities) == priorities[tmp]:
            priorities[tmp] = 0
            answer += 1
            if tmp == location:
                break
        else:
            que.append(tmp)
    return answer