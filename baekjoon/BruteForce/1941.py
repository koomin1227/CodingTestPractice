from itertools import combinations
from collections import deque
seats = []
for i in range(5):
    seats.append(input())
answer = []
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def is_connect(memebrs):
    memebrs = list(memebrs)
    que = deque()
    que.append(memebrs.pop())
    while que:
        member = que.pop()
        r = member // 5
        c = member % 5
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
                continue
            if nr * 5 + nc in memebrs:
                que.append(nr * 5 + nc)
                memebrs.remove(nr * 5 + nc)
    return len(memebrs) == 0

tmp = [i for i in range(25)]
member_list = list(combinations(tmp, 7))

answer  = 0
answer_lis = []
for memebrs in member_list:
    cnt = {'S':0, 'Y':0}
    for member in memebrs:
        r = member // 5
        c = member % 5
        cnt[seats[r][c]] += 1
        if cnt['Y'] > 3:
            break
    if cnt['Y'] > 3:
            continue
    if is_connect(memebrs):
        answer += 1
        answer_lis.append(memebrs)

print(answer)
