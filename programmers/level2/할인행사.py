def solution(want, number, discount):
    answer = 0
    dic = {}
    def check(dic,want,number):
        check = 1
        for i in range(len(want)):
            if want[i] not in dic:
                check = 0
                break
            if dic[want[i]]<number[i]:
                check = 0
                break
        return check    
    for i in range(10):
        if discount[i] not in dic:
            dic[discount[i]] = 0    
        dic[discount[i]] +=1
    leng = len(discount)
    if check(dic,want,number):
            answer+=1
    for i in range(1,leng - 9):
        dic[discount[i-1]]-=1
        if discount[i+9] not in dic:
            dic[discount[i+9]] = 0 
        dic[discount[i+9]]+=1
        if check(dic,want,number):
            answer+=1
    return answer