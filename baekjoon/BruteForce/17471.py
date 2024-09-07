from itertools import combinations
from collections import deque

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[]]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    graph.append(tmp[1:])

def create_candidates(n):
    candidates = []
    for i in range(1, n//2 + 1):
        comb = combinations(range(1, n + 1), i)
        for c in list(comb):
            other_city = []
            for j in range(1, n+1):
                if j not in c:
                    other_city.append(j)
            candidates.append([list(c), other_city])
    return candidates

def sum_section(section):
    tot = 0
    for i in section:
        tot += population[i]
    return tot

def is_all_connected(section):
    if len(section) == 0:
        return True
    is_visited = []
    que = deque()
    que.append(section[0])
    is_visited.append(section[0])
    while que:
        cur = que.popleft()
        for n in graph[cur]:
            if n not in section:
                continue
            if n in is_visited:
                continue
            is_visited.append(n)
            que.append(n)
    return len(is_visited) == len(section)

def is_possible(section1, section2):
    if not is_all_connected(section1):
        return False
    if not is_all_connected(section2):
        return False
    return True

candidates = create_candidates(n)
answer = sum(population)
is_dividable = False
for section1, section2 in candidates:
    if is_possible(section1, section2):
        is_dividable = True
        answer = min(answer, abs(sum_section(section1) - sum_section(section2)))

if is_dividable == False:
    print(-1)
else:
    print(answer)
