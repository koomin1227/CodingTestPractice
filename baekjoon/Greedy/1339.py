from sys import stdin
from collections import defaultdict
input = stdin.readline

n = int(input())
words = []
alp = defaultdict(int)
for i in range(n):
    tmp = list(input())
    tmp.pop()
    words.append(tmp)
    for j in range(len(tmp)):
        alp[tmp[j]] += 10**(len(tmp) - j)
tmp = []
for key in alp.keys():
    tmp.append([alp[key], key])

tmp.sort(reverse=True)
num = 9
for key in tmp:
    alp[key[1]] = num
    num -= 1
answer = 0
for word in words:
    num = 0
    for key in word:
        num = num * 10 + alp[key]
    answer += num
print(answer)