t = int(input())
ns = []
for i in range(t):
    ns.append(int(input()))
cases = []

def is_zero(string):
    result = 0
    oper = ''
    num = 0
    i = 0
    for i in range(len(string)):
        if string[i] == '+' or string[i] == '-':
            if oper == '':
                result = num
            elif oper == '+':
                result += num
            else:
                result -= num
            oper = string[i]
            num = 0
        elif string[i] == ' ':
            continue
        else:
            num = num*10 + int(string[i])
    if oper == '':
        result = num
    elif oper == '+':
        result += num
    else:
        result -= num
    return result == 0



def dfs(depth, opers, max_depth, nums):
    if depth == max_depth:
        string = str(nums[0])
        for i in range(len(opers)):
            string += opers[i]
            string += str(nums[i + 1])
        return cases.append(string)
    opers.append('+')
    dfs(depth + 1, opers, max_depth, nums)
    opers.pop()
    opers.append('-')
    dfs(depth + 1, opers, max_depth, nums)
    opers.pop()
    opers.append(' ')
    dfs(depth + 1, opers, max_depth, nums)
    opers.pop()

for n in ns:
    numbers = range(1, n + 1)
    cases = []
    dfs(0, [], n - 1, numbers)
    answer = []
    for case in cases:
        if is_zero(case):
            answer.append(case)
    answer.sort()
    for i in answer:
        print(i)
    print()
    
