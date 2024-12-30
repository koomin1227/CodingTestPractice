n = int(input())
points = []
for i in range(n):
    x,y = map(int, input().split())
    points.append((x,y))

points.sort()

answer = 0
left = points[0][0]
right = points[0][1]
for i in range(1, n):
    x, y = points[i]
    if left <= x <= right:
        right = max(right, y)
    else:
        answer += abs(right - left)
        left = x
        right = y
    
answer += abs(right - left)
print(answer)