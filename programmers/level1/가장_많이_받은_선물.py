def solution(friends, gifts):
    answer = 0
    gift_list = {}
    gift_value = {}
    for friend in friends:
        gift_list[friend] = {}
        gift_value[friend] = 0
        for j in friends:
            if friend != j:
                gift_list[friend][j] = [0, 0]
                
    for gift in gifts:
        a, b = gift.split(" ")
        a_list = gift_list[a]
        b_list = gift_list[b]
        a_list[b][0] += 1
        b_list[a][1] += 1
        gift_value[a] += 1
        gift_value[b] -= 1

    for key in gift_list.keys():
        total_gift = 0
        for other in gift_list[key].keys():
            if gift_list[key][other][0] > gift_list[key][other][1]:
                total_gift += 1
            elif gift_list[key][other][0] == gift_list[key][other][1]:
                if gift_value[key] > gift_value[other]:
                    total_gift += 1
        answer = max(answer, total_gift)        
    return answer