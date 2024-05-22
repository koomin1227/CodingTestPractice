from sys import stdin
from collections import defaultdict
input = stdin.readline
name = input()
dic = defaultdict(int)
for i in name:
    dic[i] += 1

keys = list(dic.keys())
keys.sort()
cnt_1  = 0
for key in keys:
    if dic[key] == 1:
        cnt_1 += 1
result = ""
if cnt_1 > 1:
    print("I'm Sorry Hansoo")
else:
    for key in keys:
        result += key
    keys.reverse()
    for key in keys:
        if dic[key] != 1:
            result += key
    print(result)