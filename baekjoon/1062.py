from sys import stdin
from itertools import combinations
input = stdin.readline

n, k = map(int, input().split())
essential_alphabet = ['a','c','n','t','i']
alphabet = set()
words = []

def count(comb):
    count = 0
    for word in words:
        is_ok = True
        for w in word:
            if w not in essential_alphabet and w  not in comb:
                is_ok = False
                break
        if is_ok:
            count += 1
    return count

for i in range(n):
    word = list(input())
    word = word[4:-5]
    words.append(word)
    for w in word:
        if w in essential_alphabet:
            continue
        alphabet.add(w)

if k < 5:
    print(0)
    exit()
if len(alphabet) == 0:
    print(n)
    exit()

if len(alphabet) <= k -5:
    print(n)
    exit()

answer = 0
combs = combinations(list(alphabet), k - 5)
for comb in combs:
    c = count(comb)
    answer = max(c, answer)

print(answer)