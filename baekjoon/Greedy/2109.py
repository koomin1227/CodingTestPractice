import heapq
n = int(input())
lec = []
for i in range(n):
    lec.append(list(map(int,input().split())))
lec.sort(key=lambda x : x[1])
s = []
for i in lec:
    heapq.heappush(s, i[0])
    if len(s) > i[1]:
        heapq.heappop(s)
print(sum(s))