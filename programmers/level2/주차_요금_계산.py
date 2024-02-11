def solution(fees, records):
    LAST_TIME = 23*60 + 59
    answer = []
    park_time = {}
    for record in records:
        time, car, kind = record.split(' ')
        m,s = time.split(':')
        time = int(m) * 60 + int(s)
        car = int(car)

        if car not in park_time:
            park_time[car] = [0, time, 'IN']
        if car in park_time:
            if kind == 'OUT':
                park_time[car][0] += time - park_time[car][1]
                park_time[car][1] = 0
                park_time[car][2] = 'OUT'
            else:
                park_time[car][1] = time
                park_time[car][2] = 'IN'
                
    price = {}
    for car in park_time.keys():
        if park_time[car][2] == 'IN':
            park_time[car][0] += LAST_TIME - park_time[car][1]
            park_time[car][1] = 0
            park_time[car][2] = 'OUT'
        price[car] = 0
        time = park_time[car][0]
        if time >= 1:
            price[car] += fees[1]
        if time - fees[0] > 0:
            tmp = (time - fees[0]) // fees[2]
            if (time - fees[0]) % fees[2] != 0:
                tmp += 1
            price[car] += tmp * fees[3]
    cars = list(park_time.keys())
    cars.sort()
    for car in cars:
        answer.append(price[car])
        
    return answer