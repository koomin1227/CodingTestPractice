from collections import deque
import heapq

n = int(input())
subjects = []
for i in range(n):
    d, w = map(int, input().split())
    subjects.append((d, w))

subjects = sorted(subjects, key=lambda x: (x[0], -x[1]))
subjects = deque(subjects)

ans = []

for i in range(n):
    d, w = subjects.popleft()
    if len(ans) < d:
        heapq.heappush(ans, (w,d))
    elif len(ans) == d:
        nw, nd = heapq.heappop(ans)
        if w > nw:
            heapq.heappush(ans, (w,d))
        else:
            heapq.heappush(ans, (nw, nd))
answer = 0
for w, d in ans:
    answer += w
print(answer)
    