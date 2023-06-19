from itertools import permutations
import math

def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
def solution(numbers):
    answer = 0
    prime = set()
    num = []
    
    for i in range(len(numbers)):
        num.append(numbers[i])
        
    for i in range(1,len(numbers)+2):
        comb = list(permutations(num, i))
        for com in comb:
            str_num = ''.join(s for s in com)
            tmp = int(str_num)
            if is_prime_number(tmp):
                prime.add(tmp)
    print(prime)
    answer = len(prime)
    return answer