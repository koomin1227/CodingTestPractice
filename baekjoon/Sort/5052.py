# https://www.acmicpc.net/problem/5052
from sys import stdin
input = stdin.readline
t = int(input())
for p in range(t):
    answer = "YES"
    n = int(input())
    phones = []
    for i in range(n):
        phones.append(input().rstrip())
    phones.sort()
    for i in range(n-1):
        if (len(phones[i]) < len(phones[i + 1])):
            short = phones[i]
            long = phones[i + 1]
        else:
            short = phones[i + 1]
            long = phones[i]
        if long.startswith(short):
            answer = "NO"
            break
    print(answer)
