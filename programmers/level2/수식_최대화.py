from itertools import permutations
import re
def solution(expression):
    
    def make_post(word, priority):
        stack = []
        post_fix = []
        for i in word:
            if i not in priority:
                post_fix.append(i)
            else:
                if len(stack) == 0:
                    stack.append(i)
                elif priority.index(stack[-1]) < priority.index(i):
                    stack.append(i)
                elif priority.index(stack[-1]) >= priority.index(i):
                    while priority.index(stack[-1]) >= priority.index(i):
                        post_fix.append(stack.pop())
                        if len(stack) == 0:
                            break
                    stack.append(i)
        while stack:
            post_fix.append(stack.pop())
        return post_fix

    def calculate(post,priority):
        stack = []
        for i in post:
            if i not in priority:
                stack.append(i)
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+': 
                    stack.append(a+b)
                elif i == '-': 
                    stack.append(a-b)
                elif i == '*': 
                    stack.append(a*b)
        return abs(stack.pop())
                
        
    answer = 0
    word = re.split("([-,+,*])", expression)
    
    oper = ['+','-','*']
    oper_set = set()
    for i in range(len(word)):
        if word[i] in oper:
            oper_set.add(word[i])
        else:
            word[i] = int(word[i])
    oper_cnt = len(oper_set)
    oper_pri = list(permutations(list(oper_set),oper_cnt))
    
    for pri in oper_pri:
        post_fix = make_post(word,pri)
        print(post_fix)
        answer = max(calculate(post_fix,pri),answer)
    return answer