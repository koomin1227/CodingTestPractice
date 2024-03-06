def solution(picks, minerals):
    answer = 0
    sections = []
    section_cnt = len(minerals) // 5
    for i in range(section_cnt):
        sections.append(minerals[5*i:5*i+5])
    if len(minerals) > 5*section_cnt:
        sections.append(minerals[section_cnt * 5:])
    order = []
    for section in sections:
        tmp = [0, 0, 0]
        for mineral in section:
            if mineral == 'diamond':
                tmp[0] += 1
            elif mineral == 'iron':
                tmp[1] += 1
            else:
                tmp[2] += 1
        order.append(tmp)
    for o in order:
        if picks
    order.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    # print(section_cnt)
    print(order)
    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
solution(picks, minerals)