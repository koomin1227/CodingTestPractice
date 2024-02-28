def dec2base(num, base):
    res = []
    if num == 0:
        return [0]
    while num > 0:
        res.append(num % base)
        num = num // base
    res.reverse()
    return res

def num2chr(num):
    chrs = ['A','B','C','D','E','F']
    if num >= 10:
        return chrs[num - 10]
    else:
        return str(num)
        

def solution(n, t, m, p):
    answer = ''
    bases = [0]
    num = 0
    for i in range(t*m):
        if len(bases) <= i:
            num += 1
            bases += dec2base(num, n)
        now = bases[i]
        if i % m == p-1:
            answer += num2chr(now)

    return answer