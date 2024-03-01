def solution(words): 
    answer = 0
    dic = {}
    for word in words:
        cur_dict = dic
        for cur_word in word:
            cur_dict.setdefault(cur_word, [0, {}])
            cur_dict[cur_word][0] += 1
            cur_dict = cur_dict[cur_word][1]
    for word in words:
        cur_dict = dic
        for char in word:
            answer += 1
            cur_dict = cur_dict[char]
            if cur_dict[0] != 1:
                cur_dict = cur_dict[1]
            else:
                break
                
    return answer