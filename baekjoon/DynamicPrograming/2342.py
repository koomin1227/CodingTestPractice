from sys import stdin
input = stdin.readline
feet = []
for i in range(5):
    for j in range(5):
        if i > 0 and i == j:
            continue
        feet.append((i, j))
def calcCost(prev, next):
    if prev == 0:
        return 2
    elif prev == next:
        return 1
    elif abs(next - prev) == 2:
        return 4
    else:
        return 3
    
def find_foot_index(target):
    for i in range(len(feet)):
        if feet[i] == target:
            return i
instructions = list(map(int, input().split()))

dp = [[-1] * len(feet) for _ in range(len(instructions) - 1)]
for i in range(len(feet)):
    foot = feet[i]
    if foot == (instructions[0], 0) or foot == (0, instructions[0]):
        dp[0][i] = 2

for i in range(1, len(instructions) - 1):
    instruction = instructions[i]
    for j in range(len(feet)):
        if dp[i - 1][j] == -1:
            continue
        foot = feet[j]
        if instruction != foot[1]:
            left = dp[i - 1][j] + calcCost(foot[0], instruction)
            if dp[i][find_foot_index((instruction, foot[1]))] == -1:
                dp[i][find_foot_index((instruction, foot[1]))] = left
            else:
                dp[i][find_foot_index((instruction, foot[1]))] = min(left, dp[i][find_foot_index((instruction, foot[1]))])
        if instruction != foot[0]:
            right = dp[i - 1][j] + calcCost(foot[1], instruction)
            if dp[i][find_foot_index((foot[0], instruction))] == -1:
                dp[i][find_foot_index((foot[0], instruction))] = right
            else:
                dp[i][find_foot_index((foot[0], instruction))] = min(right, dp[i][find_foot_index((foot[0], instruction))])
answer = 500000 
for i in dp[-1]:
    if i != -1:
        answer = min(answer, i)
print(answer)