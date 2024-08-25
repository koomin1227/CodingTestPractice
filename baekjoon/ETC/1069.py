import math
x,y,d,t = map(int, input().split())
distance = math.sqrt(pow(x, 2) + pow(y, 2))
answer = 0
if distance > d:
    answer = min(distance, t*(distance//d+1), t*(distance//d) + distance % d)
else:
    answer = min(distance, 2*t, t + d - distance)

print(answer)