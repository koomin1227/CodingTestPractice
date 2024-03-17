n = int(input())
words = []
for i in range(n):
    words.append(input())
result = 0
for word in words:
    if len(word) == 1:
        result += 1
        continue
    tmp = []
    is_group = True
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            if word[i] not in tmp:
                tmp.append(word[i])
            else:
                is_group = False
                break
    if word[-1] == word[-2] and word[-1] in tmp:
        is_group = False
    elif word[-1] != word[-2] and word[-1] in tmp:
        is_group = False

    if is_group:
        result += 1
print(result)