def solution(record):
    answer = []
    user_info = {}
    for r in record:
        tmp = r.split(' ')
        if tmp[0] != 'Leave':
            user_info[tmp[1]] = tmp[2]
    for r in record:
        tmp = r.split(' ')
        if tmp[0] == 'Enter':
            message = user_info[tmp[1]] + '님이 들어왔습니다.'
            answer.append(message)
        elif tmp[0] == 'Leave':
            message = user_info[tmp[1]] + '님이 나갔습니다.'
            answer.append(message)
        
    return answer