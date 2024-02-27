def solution(dartResult):
    answer = 0
    scores = []
    bonuses = []
    options = [0] * 3
    results = [0] * 3
    score = 0
    set_num = -1
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            score = score * 10 + int(dartResult[i])
        elif dartResult[i] in ['S', 'D', 'T']:
            bonus = dartResult[i]
            bonuses.append(bonus)
            scores.append(score)
            score = 0
            set_num += 1
        else:
            option = dartResult[i]
            options[set_num] = option
    
    for i in range(3):
        results[i] = scores[i]
        if bonuses[i] == 'D':
            results[i] = results[i]**2
        elif bonuses[i] == 'T':
            results[i] = results[i]**3
        if options[i] == '*':
            results[i] = results[i] * 2
            if i > 0:
                results[i - 1] = results[i - 1] * 2
        elif options[i] == '#':
            results[i] = results[i] * (-1)
    answer = sum(results)
    return answer