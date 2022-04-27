def solution(food_times, k):
    answer = 0
    t=1
    tmp=False
    while t!=k+2:
        if list(set(food_times))[-1]==0:
            tmp=True
            break
        if food_times[answer]!=0:
            food_times[answer]-=1
        else:
            t-=1
        if t==k+1:
            break
        answer+=1
        if answer>=len(food_times):
            answer-=len(food_times)
        t+=1
    if tmp:
        answer=-1
    else:
        answer+=1
    return answer
food=list(map(int,input().split()))
k=int(input())
print(solution(food,k))