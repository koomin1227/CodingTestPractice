# https://www.acmicpc.net/problem/1759
from sys import stdin
input = stdin.readline

l,c = map(int,input().split())
chars = list(map(str, input().split()))
vowel = ['a','e','i','o','u']
chars.sort()
ans = []
chr = [chars[0]]
def check(target):
    tot = 0
    for i in range(0, l):
        if target[i] in vowel:
            tot += 1
    if tot >= 1 and l - tot >= 2:
        return True
    else:
        return False
def dfs(depth, n):
    if depth == l-1:
        if check(chr):
            print(''.join(s for s in chr))
        return
    for i in range(n+1,c):        
        chr.append(chars[i])
        dfs(depth + 1, i)
        chr.pop()
for i in range(0,(c - l) + 1):
    chr = [chars[i]]
    dfs(0, i)

