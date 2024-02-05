# 시간 초과
def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        deli_cap = cap
        pick_cap = cap
        max_move = 0
        for i in range(n - 1, -1, -1):
            if deliveries[i] > 0 and deli_cap > 0:
                if deliveries[i] > deli_cap:
                    deliveries[i] -= deli_cap
                    deli_cap = 0
                else:
                    deli_cap = deli_cap - deliveries[i] 
                    deliveries[i] = 0
                max_move = max(max_move, i + 1)
            if pickups[i] > 0 and pick_cap > 0:
                if pickups[i] > pick_cap:
                    pickups[i] -= pick_cap
                    pick_cap = 0
                else:
                    pick_cap = pick_cap - pickups[i] 
                    pickups[i] = 0
                max_move = max(max_move, i + 1)

        # print(deliveries)
        # print(pickups)
        # print(max_move)
        answer += 2 * max_move
        if deli_cap == cap and pick_cap == cap:
            break
            
    return answer

## 정답
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()
    
    deli_cap = 0
    pick_cap = 0
    
    for i in range(n):
        deli_cap += deliveries[i]
        pick_cap += pickups[i]
        
        while deli_cap > 0 or pick_cap > 0:
            deli_cap -= cap
            pick_cap -= cap
            answer += 2 * (n - i)
            
    return answer