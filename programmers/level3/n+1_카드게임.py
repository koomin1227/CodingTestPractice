from collections import deque
from itertools import combinations
def solution(coin, cards):
    answer = 0
    n = len(cards)
    picked_cards = cards[:n//3]
    cards = deque(cards[n//3:])
    
    def is_13(nums, n):
        combs = list(combinations(nums, 2))
        for comb in combs:
            if sum(comb) == n+1:
                return comb
        return []
    draw_cards = []
    while True:
        answer += 1
        if len(cards) == 0:
            break
        draw_cards.append(cards.popleft())
        draw_cards.append(cards.popleft())
        
        res = is_13(picked_cards, n)
        if len(res) != 0:
            a,b = res
            picked_cards.remove(a)
            picked_cards.remove(b)
            continue
        if coin >= 1:
            is_continue = False
            for j in draw_cards:
                for i in picked_cards:
                    if j + i == n + 1:
                        picked_cards.remove(i)
                        draw_cards.remove(j)
                        coin -= 1
                        is_continue = True
                        break
                if is_continue:
                    break
            if is_continue:
                continue
        if coin >= 2:
            res = is_13(draw_cards, n)
            if len(res) != 0:
                a,b = res
                draw_cards.remove(a)
                draw_cards.remove(b)
                coin -= 2
                continue
        break
            

    # print(picked_cards)
    # print(cards)
    print(answer)
    return answer

coin = 4
cards = [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]
solution(coin, cards)