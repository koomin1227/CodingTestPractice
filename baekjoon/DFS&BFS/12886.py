from collections import deque

rocks = list(map(int, input().split()))

combinations = [(0, 1, 2), (1, 2, 0), (0, 2, 1)]
visited = set()
queue = deque([tuple(rocks)])
visited.add(tuple(rocks))

is_possible = False

while queue:
    current = queue.popleft()

    if current[0] == current[1] == current[2]:
        is_possible = True
        break

    for a, b, c in combinations:
        next_rock = list(current)

        if current[a] < current[b]:
            next_rock[a] = current[a] * 2
            next_rock[b] = current[b] - current[a]
        elif current[a] > current[b]:
            next_rock[b] = current[b] * 2
            next_rock[a] = current[a] - current[b]
        else:
            continue

        next_state = tuple(next_rock)
        if next_state not in visited:
            queue.append(next_state)
            visited.add(next_state)

print(1 if is_possible else 0)