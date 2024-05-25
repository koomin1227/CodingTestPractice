from collections import deque
import math
n, m, r = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

start = [0,0]
end = [n, m]
while start[0] < math.ceil(n / 2) and start[1] < math.ceil(m / 2):
    deq = deque([])
    for i in range(start[1], end[1] - 1):
        deq.append(arr[start[0]][i])
    for i in range(start[0], end[0] - 1):
        deq.append(arr[i][end[1] - 1])
    for i in range(end[1] - 1, start[1], -1):
        deq.append(arr[end[0] - 1][i])
    for i in range(end[0] - 1, start[0], -1):
        deq.append(arr[i][start[1]])

    deq.rotate((r % len(deq)) * -1)

    for i in range(start[1], end[1] - 1):
        arr[start[0]][i] = deq.popleft()
    for i in range(start[0], end[0] - 1):
        arr[i][end[1] - 1] = deq.popleft()
    for i in range(end[1] - 1, start[1], -1):
        arr[end[0] - 1][i] = deq.popleft()
    for i in range(end[0] - 1, start[0], -1):
        arr[i][start[1]] = deq.popleft()

    start[0] += 1
    start[1] += 1
    end[0] -= 1
    end[1] -= 1
for i in arr:
    for j in i:
        print(j, end=' ')
    print()
