n,k = map(int, input().split())
order = list(map(int,input().split()))
multitab = [0] * n
extract_cnt = 0

def find_extract(cur_order, elec):
    # 제일 나중에 사용될 또는 사용되지 않는 용품을 뽑는다
    left_order = order[cur_order + 1:]
    max_use = [-1, -1]
    for i in range(len(multitab)):
        if multitab[i] not in left_order:
            return i
        else:
            idx = left_order.index(multitab[i])
            if max_use[1] < idx:
                max_use[0] = i
                max_use[1] = idx
    return max_use[0]
for i in range(k):
    if order[i] in multitab:
        continue
    if 0 in multitab:
        idx = multitab.index(0)
        multitab[idx] = order[i]
        continue
    else:
        idx = find_extract(i, order[i])
        multitab[idx] = order[i]
        extract_cnt += 1

print(extract_cnt)