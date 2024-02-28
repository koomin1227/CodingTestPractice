def init_dict():
    dict = {}
    index = 1
    ord_num = ord('A')
    for i in range(26):
        dict[chr(ord_num + i)] = index
        index += 1
    return dict

def solution(msg):
    answer = []
    dict = init_dict()
    index = 27
    
    i = 0
    while True:
        for j in range(i, len(msg)):
            is_end = False
            target = msg[i:j + 1]
            if target not in dict:
                answer.append(dict[msg[i:j]])
                if target not in dict:
                    dict[target] = index
                    index += 1
                i = j
                is_end = True
                break
        if is_end == False:
            answer.append(dict[target])
            break
    return answer