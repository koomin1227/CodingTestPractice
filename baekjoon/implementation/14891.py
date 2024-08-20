from collections import deque
# 2 오 6 왼
def turnClock(gear):
    gear.appendleft(gear.pop())
    return gear

def turnAntiClock(gear):
    gear.append(gear.popleft())
    return gear

gears = []
for _ in range(4):
    tmp = input()
    gears.append(deque([int(num) for num in tmp]))

k = int(input())
methods = []
for _ in range(k):
    n, d = map(int, input().split())
    methods.append([n - 1, d])

# 2
for n, d in methods:
    spinGear = [0,0,0,0]
    spinGear[n] = d
    if n != 0:
        for i in range(n - 1, -1, -1):
            if gears[i][2] != gears[i + 1][6]:
                spinGear[i] = spinGear[i+1] * -1
    if n != 3:
        for i in range(n + 1, 4):
            if gears[i][6] != gears[i - 1][2]:
                spinGear[i] = spinGear[i - 1] * -1
    for i in range(4):
        if spinGear[i] == 1:
            gears[i] = turnClock(gears[i])
        elif spinGear[i] == -1:
            gears[i] = turnAntiClock(gears[i])

    # print(spinGear)

score = 0
if gears[0][0] == 1:
    score += 1
if gears[1][0] == 1:
    score += 2
if gears[2][0] == 1:
    score += 4
if gears[3][0] == 1:
    score += 8
print(score)

