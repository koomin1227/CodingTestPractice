from sys import stdin
from collections import defaultdict
input=stdin.readline

n = int(input())
string = list(input())

l = 0
r = 0
alphabet = defaultdict(int)
alphabet[string[l]] += 1

max_len = 1

while r < len(string) - 1:
    if len(alphabet) <= n:
        max_len = max(max_len, r - l + 1)
        r += 1
        alphabet[string[r]] += 1
    else:
        alphabet[string[l]] -= 1
        if alphabet[string[l]] == 0:
            del alphabet[string[l]]
        l += 1
print(max_len)
