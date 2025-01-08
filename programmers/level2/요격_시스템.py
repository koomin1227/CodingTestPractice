def solution(targets):
    answer = 0
    targets.sort(reverse = True)
    left = targets[0][0]
    right = targets[0][1]
    section_count = 1
    while targets:
        now = targets.pop()
        if now[0] < right:
            left = max(left, now[0])
            right = min(right, now[1])
        else:
            answer += section_count
            left = now[0]
            right = now[1]
            section_count = 1
    answer += section_count
    return answer