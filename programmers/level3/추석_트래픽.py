def time_to_milliseconds(time_str):
    time_parts = time_str.split(':')
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds, milliseconds = map(float, time_parts[2].split('.'))
    total_milliseconds = int((hours * 3600 + minutes * 60 + seconds) * 1000 + milliseconds)
    return total_milliseconds

def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt

def solution(lines):
    answer = 0
    res = [0] * 86400000
    times = []
    for line in lines:
        date, time, process_time = line.split(' ')
        end_time = time_to_milliseconds(time)
        start_time = end_time - int(float(process_time[:-1]) * 1000) + 1
        times.append((start_time, end_time))
    for x in times:
        answer = max(answer, throughput(times, x[0], x[0] + 1000), throughput(times, x[1], x[1] + 1000))
    return answer