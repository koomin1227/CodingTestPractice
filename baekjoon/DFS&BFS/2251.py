from collections import deque
a,b,c = map(int, input().split())

max_capacity = [a, b, c]

que = deque()
answer = [c]
que.append((0,0,c))
visited = [(0,0,c)]
while que:
    now_bottles = que.popleft()
    if now_bottles[2] not in answer and now_bottles[0] == 0:
        answer.append(now_bottles[2])
    # i -> j 로 물을 옮긴다.
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if now_bottles[i] == 0:
                continue
            if max_capacity[j] == now_bottles[j]:
                continue
            remain_capacity_j = max_capacity[j] - now_bottles[j]
            new_bottle = [now_bottles[0], now_bottles[1], now_bottles[2]]
            if now_bottles[i] >= remain_capacity_j:
                new_bottle[j] = max_capacity[j]
                new_bottle[i] = new_bottle[i] - remain_capacity_j
            else:
                new_bottle[j] = new_bottle[j] + new_bottle[i]
                new_bottle[i] = 0
            new_bottle_tuple = (new_bottle[0], new_bottle[1], new_bottle[2])
            if new_bottle_tuple not in visited:
                visited.append(new_bottle_tuple)
                que.append(new_bottle_tuple)

answer.sort()
for i in answer:
    print(i, end=" ")