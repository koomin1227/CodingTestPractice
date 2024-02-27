def dec2bin(num, n):
    res= []
    for i in range(n):
        if num % 2 == 0:
            res.append(' ')
        else:
            res.append('#')
        num = num // 2
    res.reverse()
    return "".join(res)

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        res = arr1[i] | arr2[i]
        answer.append(dec2bin(res, n))
        
    return answer