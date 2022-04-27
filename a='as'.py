def solution(id_list, report, k):
    answer = [0]*len(id_list)
    ind={}
    for i in id_list:
        ind[i]=set()
    for i in set(report):
        report_id,reported_id=i.split()
        ind[reported_id].add(report_id)

    for i in ind.keys():
        if len(ind[i])>=k:
            for j in ind[i]:
               answer[id_list.index(j)]+=1
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