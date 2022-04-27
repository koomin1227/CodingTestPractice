def solution(id_list, report, k):
    answer = []
    ind={}
    a=0
    for i in id_list:
        ind[i]=[]
        ind[i].append([])#신고한 id
        ind[i].append([])#정지된 id
        ind[i].append([])#신고당한 id
        a+=1
    for i in report:
        report_id,reported_id=i.split()
        tmp=0
        for j in ind[report_id][0]:
            if j==reported_id:
                tmp=1
        if tmp==0:
            ind[report_id][0].append(reported_id)
        for j in ind[reported_id][0]:
            if j==report_id:
                tmp=1
        if tmp==0:
            ind[reported_id][2].append(report_id)
            
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