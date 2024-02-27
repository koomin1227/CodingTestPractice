def solution(n, t, m, timetable):
    answer = 0
    times = []
    bus_times = []
    for i in range(n):
        bus_times.append(540 + t * i)
    for time in timetable:
        h,mi = time.split(':')
        minute = int(h) * 60 + int(mi)
        times.append(minute)
    times.sort()
    
    now = 0
    for bus_time in bus_times:
        passenger = 0
        while int(passenger) < int(m) and now < len(times):
            if times[now] <= bus_time:
                passenger += 1
                now+= 1
            else:
                break
    if passenger < m:
        answer = bus_time
    else:
        answer = times[now - 1] - 1      

    h = int(answer)//60
    mi = int(answer)%60
    if len(str(h)) == 1:
        h = '0' + str(h)
    if len(str(mi)) == 1:
        mi = '0' + str(mi)
    answer = str(h) + ':' + str(mi)
    return answer