def solution(food_times, k):
    answer = 0
    num=0
    tmp=False
    k=k+1
    p=1
    qwe=-1
    mini1=min(food_times)
    for i in food_times:
        if i!=0:
            num+=1
    while True:
        if num==0 and k==0:
            qwe=p
            break
        if num<k and num!=0:
            if k>mini1*num and num!=0:
                k=k-(mini1*num)
            else:
                mini1=k//num
                k=k-(num*(k//num))
        else:
            break

        
        num=0
        mini2=100000000
        for i in range(len(food_times)):
            if food_times[i]!=0:
                food_times[i]-=mini1
                p=i
                if food_times[i]!=0:
                    if food_times[i]<=mini2:
                        mini2=food_times[i]
                    num+=1
        mini1=mini2
    if k!=0:
        for i in range(len(food_times)):
            if food_times[i]!=0:
                k-=1
            if k==0:
                tmp=True
                break
    if qwe!=-1:
        tmp=True
        answer=qwe
    if tmp:
        answer=i+1
    else:
        answer=-1       
    return answer
food=list(map(int,input().split()))
k=int(input())
print(solution(food,k))