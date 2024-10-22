from collections import deque
def convert_to_minute(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def solution(plans):
    answer = []
    ordered_subject = []
    stop_subject = deque()
    for name, start_time, time in plans:
        ordered_subject.append([convert_to_minute(start_time), int(time), name])
    ordered_subject.sort()
    ordered_subject = deque(ordered_subject)
    
    now = ordered_subject[0][0]
    playing_subject = None
    
    while len(answer) != len(plans):
        if playing_subject != None:
            playing_subject[1] -= 1
            if playing_subject[1] == 0:
                answer.append(playing_subject[2])
                if len(stop_subject) > 0:
                    playing_subject = stop_subject.pop()
        
        if len(ordered_subject) > 0 and ordered_subject[0][0] == now:
            if playing_subject != None:
                stop_subject.append(playing_subject)
            playing_subject = ordered_subject.popleft()
        now += 1

    return answer
