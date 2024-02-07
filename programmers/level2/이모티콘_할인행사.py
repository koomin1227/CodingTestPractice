from itertools import product
def solution(users, emoticons):
    answer = []
    max_plus = 0
    max_price = 0
    dis_comb = list(product([10,20,30,40], repeat=len(emoticons)))
    for discount in dis_comb:
        plus = 0
        price = 0
        for user in users:
            user_price = 0
            for i in range(len(emoticons)):
                if discount[i] >= user[0]:
                    user_price += emoticons[i] * (100 - discount[i]) / 100
            if user[1] <= user_price:
                plus += 1
            else:
                price += user_price
        if max_plus < plus:
            max_plus = plus
            max_price = price
        elif max_plus == plus and max_price < price:
            max_price = price
    
    # print(dis_comb)
    return [max_plus, int(max_price)]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

print(solution(users, emoticons))