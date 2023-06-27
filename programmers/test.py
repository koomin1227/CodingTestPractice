def solution(r1, r2):
    answer = 0
    r11 = ((2*r1)-1) * ((2*r1)-1)
    r22 = ((2*r2)-1) * ((2*r2)-1)
    answer = (r22 - r11) + 4
    return answer
print(solution(2,4))