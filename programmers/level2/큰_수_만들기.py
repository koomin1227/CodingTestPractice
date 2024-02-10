def solution(number, k):
    numbers = list(number)
    stack = []
    for number in numbers:
        while stack and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1
        stack.append(number)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)
