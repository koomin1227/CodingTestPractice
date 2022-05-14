def turn_snake(spin_info,time,snake_info):
    for t in spin_info:
        if t[0]==time:
            if t[1]=='D':
                snake_info[0][2]-=1
                if snake_info[0][2]==-1:
                    snake_info[0][2]=3
            else:
                snake_info[0][2]+=1
                if snake_info[0][2]==4:
                    snake_info[0][2]=0
            break
    return snake_info[0][2]
    
apple_info=[]
spin_info=[]
way=[(-1,0),(0,-1),(1,0),(0,1)]#uldr
snake_info=[[1,1,3]]#행 열 방향
time=0
tail_count=0
tail_judge=0
tmp=0
n=int(input())
k=int(input())
for i in range(k):
    a=list(map(int,input().split()))
    apple_info.append(a)
l=int(input())
for i in range(l):
    a,b=map(str,input().split())
    c=[int(a),b]
    spin_info.append(c)

while True:
    time+=1
    tail_judge=0
    snake_info.insert(0,[snake_info[0][0]+way[snake_info[0][2]][0],snake_info[0][1]+way[snake_info[0][2]][1],snake_info[0][2]])
    snake_info[0][2]=turn_snake(spin_info,time,snake_info)
    if snake_info[0][0]<1 or snake_info[0][0]>n:
        break
    elif snake_info[0][1]<1 or snake_info[0][1]>n:
        break
    for tail in snake_info[1:]:
        if snake_info[0][0]==tail[0] and snake_info[0][1]==tail[1]: 
            tmp=1
            break
    if tmp==1:
        break
    for i in range(0,len(apple_info)):
        if snake_info[0][0]==apple_info[i][0] and snake_info[0][1]==apple_info[i][1]:
            tail_judge=1
            del apple_info[i]
            break
    if tail_judge==0:
        del snake_info[-1]   
        tail_judge=0   

print(time)

   
    

