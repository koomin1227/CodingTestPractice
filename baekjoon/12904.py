s = input()
t = input()

s = list(s)
t = list(t)

while len(t) != len(s):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()

isPossible = True
for i in range(len(s)):
    if s[i] != t[i]:
        isPossible = False
        break


if isPossible:
    print(1)
else:
    print(0)