def decimal_to_base(n, base):
    if n == 0:
        return "0"
    
    digits = []
    
    # n진법 변환을 위한 반복
    while n:
        digits.append(str(n % base))  # 나머지를 구해 각 자리 숫자를 저장
        n //= base  # n을 base로 나눈 몫으로 업데이트
    
    # 계산된 자릿수를 뒤집어서 반환
    return ''.join(digits[::-1])

def convert_to_10(n_str, base):
    decimal_value = 0
    power = 0

    # 역순으로 각 자리를 처리 (n진수의 자릿수에 맞게 10진수 계산)
    for digit in reversed(n_str):
        decimal_value += int(digit) * (base ** power)
        power += 1
    
    return decimal_value
def find_correct_bases(expression, minimum_base):
    bases = set()
    for i in range(minimum_base, 10):
        a = convert_to_10(expression[0], i)
        b = convert_to_10(expression[2], i)
        c = convert_to_10(expression[4], i)
        if expression[1] == '+':
            if a+b==c:
                bases.add(i)
        else:
            if a - b == c:
                bases.add(i)
    return bases
    
def solution(expressions):

    minimum_degree = 2


    full_expressions = []
    unfull_expressions = []
    for expression in expressions:
        elements = expression.split(" ")
        is_full = True
        parsed_expression = []
        for element in elements:
            if element in ["+", "-", "="]:
                parsed_expression.append(element)
            elif element == "X":
                parsed_expression.append(element)
                is_full = False
            else:
                for char in element:
                    minimum_degree = max(minimum_degree, int(char) + 1)
                parsed_expression.append(element)
        if is_full:
            full_expressions.append(parsed_expression)
        else:
            unfull_expressions.append(parsed_expression)
    bases = set([2,3,4,5,6,7,8,9])

    for expression in full_expressions:
        a = find_correct_bases(expression, minimum_degree)
        bases = bases.intersection(a)
        # print(a)
    answer = []
    # print(bases)
    
    for expression in unfull_expressions:
        candidates = set()
        for base in bases:
            a = convert_to_10(expression[0], base)
            b = convert_to_10(expression[2], base)
            if expression[1] == '+':
                c = a + b
            else:
                c = a - b
            candidates.add(decimal_to_base(c, base))
        if len(candidates) == 1:
            expression[4] = candidates.pop()
            ans = " ".join(expression)
            answer.append(ans)
        else:
            expression[4] = '?'
            ans = " ".join(expression)
            answer.append(ans)
        # print(candidates)

    # print(full_expressions)
    # print(unfull_expressions)
    # print(minimum_degree)
    return answer




# expressions = ["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]
# expressions = ["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]
expressions = ["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]
# expressions = ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]
# expressions = ["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]
print(solution(expressions))