def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack)>0:
                stack.pop() 
            else:
                answer=False
                break
    if answer == False:
        return False
    else:
        if len(stack) == 0:
            return True
        else:
            return False