def solution(survey, choices):
    answer = ''
    personality = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        score = choices[i] - 4
        if score < 0:
            personality[a] += score * (-1)
        elif score > 0:
            personality[b] += score
    keys = list(personality.keys())
    for i in range(4):
        a, b = keys[2 * i], keys[2 * i + 1]
        if personality[a] >= personality[b]:
            answer += a
        else:
            answer += b    
    return answer