from collections import deque

def dec2bin(num):
    bin = []
    while num != 0:
        bin.append(num%2)
        num = num // 2
    return bin

def dfs(now, bin, tmp, depth):
    if now % 2 == 0:
        return tmp
    
    left = now - (2 ** depth)
    right = now + (2 ** depth)
    if bin[now] == 0 and (bin[left] == 1 or bin[right] == 1):
        return False
    if dfs(left, bin, tmp, depth - 1) == False:
        tmp = False
    if dfs(right, bin, tmp, depth - 1) == False:
        tmp = False
    return tmp
    
    
def solution(numbers):
    answer = []
    for number in numbers:
        bin = dec2bin(number)
        bin_len = len(bin)
        h = 0
        while True:
            h += 1
            node_cnt = (2**h) - 1
            if node_cnt >= bin_len:
                break
        for _ in range(node_cnt- bin_len):
            bin.append(0)
        is_tree = dfs(node_cnt//2, bin, True, h - 2)
        if is_tree:
            answer.append(1)
        else:
            answer.append(0)
    return answer