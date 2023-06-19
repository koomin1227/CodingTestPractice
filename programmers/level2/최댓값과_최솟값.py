def solution(s):
    answer = ''
    num_str = s.split(" ")
    num = []
    for i in num_str:
        num.append(int(i))  
    answer += str(min(num))
    answer += " "
    answer += str(max(num))
    print(max(num))
    return answer