def solution(id_list, report, k):
    answer = []
    ind={}
    a=0
    for i in id_list:
        ind[i]=[]
        ind[i].append(set())#신고한 id
        ind[i].append([])#정지된 id
        ind[i].append(set())#신고당한 id
        a+=1
    repor=set(report)
    for i in report:
        report_id,reported_id=i.split()
        ind[report_id][0].add(reported_id)
        ind[reported_id][2].add(report_id)

    for i in ind.keys():
        if len(ind[i][2])>=k:
            for j in ind.keys():
                if i!=j:
                    for t in ind[j][0]:
                        if t==i:
                            ind[j][1].append(i)
    for i in id_list:
        answer.append(len(ind[i][1]))



        
    return answer

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2

"""
id_list=["con", "ryan"]
report=["ryan con", "ryan con", "ryan con", "ryan con"]
k=3
"""

print(solution(id_list,report,k))