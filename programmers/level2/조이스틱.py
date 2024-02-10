def solution(name):
    answer = 0
    names = list(name)
    min_move = len(name) - 1
    for i in range(len(names)):
        dif = ord('Z') - ord(names[i])
        if (dif)  < 13:
            answer += dif + 1
        else:
            answer += 25 - dif
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    
    return answer + min_move