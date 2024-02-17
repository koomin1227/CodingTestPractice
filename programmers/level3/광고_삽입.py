def time_to_sec(time):
    sec = 0
    h,m,s = time.split(':')
    sec = int(s) + (int(m) * 60) + (int(h) * 3600)
    return sec

def solution(play_time, adv_time, logs):
    answer = ''
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    table = [0] * (play_time + 2)
    
    for log in logs:
        s_time, e_time = log.split('-')
        s_time = time_to_sec(s_time)
        e_time = time_to_sec(e_time)
        table[s_time] += 1
        table[e_time] -= 1
    
    for i in range(1, len(table)):
        table[i] = table[i] + table[i - 1]
    
    i ,j = 0, adv_time - 1
    max_time = sum(table[i:j+1])
    max_time_s = 0
    cur_time = max_time
    while j <= play_time:
        cur_time -= table[i]
        cur_time += table[j + 1]
        i += 1
        j += 1
        if max_time < cur_time:
            max_time = cur_time
            max_time_s = i
    h = max_time_s // 3600
    m = (max_time_s % 3600) // 60
    s = (max_time_s % 3600) % 60
    
    result = [0] * 8
    result[0] = str(h // 10)
    result[1] = str(h % 10)
    result[2] = ':'
    result[3] = str(m // 10)
    result[4] = str(m % 10)
    result[5] = ':'
    result[6] = str(s // 10)
    result[7] = str(s % 10)
    
    answer = ''.join(result)
    return answer