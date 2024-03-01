def solution(bandage, health, attacks):
    answer = 0
    attack_dict = {attack[0] : attack[1] for attack in attacks}
    max_time = max(attack_dict.keys())
    con_suc = 0
    cur_health = health
    time = 0
    
    while time < max_time:
        time += 1
        # 공격 받는 경우
        if time in attack_dict:
            cur_health -= attack_dict[time]
            con_suc = 0
            if cur_health <= 0:
                return -1
            continue

        cur_health += bandage[1]
        con_suc += 1
        if con_suc == bandage[0]:
            con_suc = 0
            cur_health += bandage[2]
        if cur_health > health:
            cur_health = health

    return cur_health