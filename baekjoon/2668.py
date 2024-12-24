n = int(input())
table = [0]
for i in range(n):
    table.append(int(input()))

def is_circle(is_visited):
    for j in range(1, n+1):
        if is_visited[j] == 1:
            return False
    return True

answer = []
for i in range(1, n+1):
    if i in answer:
        continue
    is_visited = [0] * (n+1)
    cur = i
    is_visited[cur] += 1
    while True:
        next_num = table[cur]
        is_visited[next_num] += 1
        cur = next_num
        if is_visited[next_num] == 3:
            if is_circle(is_visited):
                for j in range(1, n+1):
                    if is_visited[j] != 0:
                        answer.append(j)
            break

answer.sort()
print(len(answer))
for i in answer:
    print(i)
            