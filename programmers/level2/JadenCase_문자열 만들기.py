def solution(s):
    s=s.lower()
    answer = ''
    word = list(s)
    for i in range(len(word)):
        if i == 0 or (word[i] != ' ' and word[i-1] == ' '):
            if ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z'):
                word[i] = chr(ord(word[i]) + ord('A') - ord('a'))
    answer = ''.join(j for j in word)   
    return answer

