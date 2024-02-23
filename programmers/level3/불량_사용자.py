from itertools import permutations
def is_same(ban, user):
    if len(ban) != len(user):
        return False
    same = True
    for i in range(len(ban)):
        if ban[i] == user[i] or ban[i] == '*':
            continue
        same = False
        break
    return same

def solution(user_id, banned_id):
    answer = []
    perms = permutations(user_id, len(banned_id))
    for perm in perms: 
        same = True
        for i in range(len(perm)):
            if is_same(banned_id[i], perm[i]):
                continue
            same = False
            break
        tmp = set(perm)
        if same and tmp not in answer:
            answer.append(tmp)
    return len(answer)