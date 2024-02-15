def solution(new_id):
    # 1.
    new_id = new_id.lower()
    
    new_id = list(new_id)
    # 2.
    answer = []
    for i in range(len(new_id)):
        if new_id[i] in ['-', '_', '.'] or (ord('a') <= ord(new_id[i]) <= ord('z')) or (ord('0') <= ord(new_id[i]) <= ord('9')):
            answer.append(new_id[i])
    # 3.
    answer3 = [answer[0]]
    for i in range(1, len(answer)):
        if answer[i] == '.' and answer[i - 1] == '.':
            continue
        answer3.append(answer[i])
    # 4.
    if len(answer3) > 0 and answer3[0] == '.':
        answer3.pop(0)
    if len(answer3) > 0 and answer3[-1] == '.':
        answer3.pop()  
    
    # 5.
    if len(answer3) == 0:
        answer3.append('a')
    
    # 6.
    if len(answer3) >= 16:
        answer3 = answer3[:15]
        if len(answer3) > 0 and answer3[-1] == '.':
            answer3.pop()  
    
    if len(answer3) <= 2:
        add_chr = [answer3[-1]] * (3 - len(answer3))
        answer3 = answer3 + add_chr
        
    return ''.join(answer3)