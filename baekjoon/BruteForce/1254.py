s = list(input())
ans = 101
s_len = len(s)//2
is_pali = True
for j in range(len(s)//2):
    if s[len(s) - j - 1] == 0:
        continue
    if s[j] == s[len(s) -j - 1]:
        continue
    elif s[j] != s[len(s) - j - 1]:
        is_pali = False
        break
if is_pali:
    ans = min(ans, len(s))
for i in range(50):
    s.append(0)
    s_len = len(s)//2
    is_pali = True
    for j in range(len(s)//2):
        if s[len(s) - j - 1] == 0:
            continue
        if s[j] == s[len(s) -j - 1]:
            continue
        elif s[j] != s[len(s) -j - 1]:
            is_pali = False
            break
    if is_pali:
        ans = min(ans, len(s))


print(ans)