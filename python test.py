def solution(n, build_frame):
    answer = []
    wall=[[-1]*(n+1) for _ in range(n+1)]#-1:빈상태 0:기둥 1:보 2:기둥,보
    for frame in build_frame:
        if frame[3]==1:#설치
            if frame[2]==0:#기둥
                if frame[1]==0 or wall[frame[1]-1][frame[0]]==0 or wall[frame[1]-1][frame[0]]==2 or wall[frame[1]][frame[0]-1]==1:#기둥 설치
                    if wall[frame[1]][frame[0]]==1:
                        wall[frame[1]][frame[0]]=2
                    else:
                        wall[frame[1]][frame[0]]=0
            else:#보
                if wall[frame[1]-1][frame[0]]==0 or wall[frame[1]-1][frame[0]+1]==0 or wall[frame[1]-1][frame[0]]==2 or wall[frame[1]-1][frame[0]+1]==2 or (wall[frame[1]][frame[0]-1]==1 and wall[frame[1]][frame[0]+1]==1):
                    if wall[frame[1]][frame[0]]==0:
                        wall[frame[1]][frame[0]]=2
                    else:
                        wall[frame[1]][frame[0]]=1
            
        else:#삭제
            if frame[2]==0:
                if wall[frame[1]+1][frame[0]]==-1:
                    if wall[frame[1]][frame[0]]==2:
                        wall[frame[1]+1][frame[0]]=1
                    else:
                        wall[frame[1]+1][frame[0]]=-1
                elif wall[frame[1]+1][frame[0]]==1 and (wall[frame[1]+1][frame[0]-1]==0 or wall[frame[1]+1][frame[0]-1]==2 or ) :
            #pass
    #print(wall)
    for i in range(n+1):
        for j in range(n+1):
            if wall[j][i]==0 or wall[j][i]==1:
                answer.append([i,j,wall[j][i]])
            elif wall[j][i]==2:
                answer.append([i,j,0])
                answer.append([i,j,1])


    return answer







n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n,build_frame))
print("qweqwee")