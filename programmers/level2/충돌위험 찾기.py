from collections import defaultdict

def count_duplicates(positions):
    counts = defaultdict(int)
    
    for pos in positions:
        counts[pos] += 1
    
    duplicates = sum(1 for count in counts.values() if count >= 2)
    
    return duplicates

def move_robot(destination, y, x):
    if destination[0] != y:
        if destination[0] < y:
            y -= 1
        else:
            y += 1
    else:
        if destination[1] < x:
            x -= 1
        else:
            x += 1
    return (y, x)

def get_next_route(destination, y, x, visited, i, routes_len):
    if y == destination[0] and x == destination[1]:
        if visited[i] == routes_len - 1:
            return -1
        else:
            return visited[i] + 1
    return visited[i]

def is_all_visit(visited):
    is_all_visit = True
    for v in visited:
        if v != -1:
            is_all_visit = False
            break
    return is_all_visit

def solution(points, routes):
    answer = 0
    time = 0
    rx = len(routes)
    next_routes = []
    positions = []
    for i in range(rx):
        next_routes.append(1)
        positions.append((points[routes[i][0] - 1][0], points[routes[i][0] - 1][1]))
        
    answer += count_duplicates(positions)
    
    while True:
        time += 1
        for i in range(rx):
            if next_routes[i] == -1:
                positions[i] = (i * -1, i * -1)
                continue
                
            destination = points[routes[i][next_routes[i]] - 1]
            y, x = positions[i]
            
            positions[i] = move_robot(destination, y, x)
            next_routes[i] = get_next_route(destination, positions[i][0], positions[i][1], next_routes, i, len(routes[0]))
            
        answer += count_duplicates(positions)
        
        if is_all_visit(next_routes):
            break

    return answer

# points = [[3, 2], [6, 4], [4, 7], [1, 4]]
# routes = [[4, 2], [1, 3], [2, 4]]
points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [4, 2], [4, 3]]
# points = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]]
# routes = [[2, 3, 4, 5], [1, 3, 4, 5]]
print(solution(points, routes))