from sys import stdin
from collections import deque
from itertools import product
import copy
import heapq
input=stdin.readline
n,m=map(int,input().split())
mop=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    mop.append(tmp)
tetro1=[[1,1,1,1]]
tetro2=[[1,1],[1,1]]
tetro3=[[1,0],[1,0],[1,1]]
tetro4=[[1,0],[1,1],[0,1]]
tetro5=[[1,1,1],[0,1,0]]
tetro6=[[0,1],[0,1],[1,1]]
tetro7=[[0,1],[1,1],[1,0]]
def rotation(target):#90 반시계 방향으로 회전
    x=len(target)
    y=len(target[0])
    new=[[0]*x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            new[y-1-j][i]=target[i][j]
    return new

# def symmetry(target):#대칭


#tetro1
maxi=0
for _ in range(2):
    tetro1=rotation(tetro1)
    for i in range(n-len(tetro1)+1):
        for j in range(m-len(tetro1[0])+1):
            tot=0

            for x in range(len(tetro1)):
                for y in range(len(tetro1[0])):
                    if tetro1[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)
#tetro2
for i in range(n-len(tetro2)+1):
    for j in range(m-len(tetro2[0])+1):
        tot=0

        for x in range(len(tetro2)):
            for y in range(len(tetro2[0])):
                if tetro2[x][y]==1:
                    tot+=mop[i+x][j+y]
                    maxi=max(maxi,tot)   

#tetro3
for _ in range(4):
    tetro3=rotation(tetro3)
    for i in range(n-len(tetro3)+1):
        for j in range(m-len(tetro3[0])+1):
            tot=0

            for x in range(len(tetro3)):
                for y in range(len(tetro3[0])):
                    if tetro3[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)     

for _ in range(2):
    tetro4=rotation(tetro4)
    for i in range(n-len(tetro4)+1):
        for j in range(m-len(tetro4[0])+1):
            tot=0

            for x in range(len(tetro4)):
                for y in range(len(tetro4[0])):
                    if tetro4[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)    

for _ in range(4):
    tetro5=rotation(tetro5)
    for i in range(n-len(tetro5)+1):
        for j in range(m-len(tetro5[0])+1):
            tot=0

            for x in range(len(tetro5)):
                for y in range(len(tetro5[0])):
                    if tetro5[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)   

for _ in range(4):
    tetro6=rotation(tetro6)
    for i in range(n-len(tetro6)+1):
        for j in range(m-len(tetro6[0])+1):
            tot=0

            for x in range(len(tetro6)):
                for y in range(len(tetro6[0])):
                    if tetro6[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)  

for _ in range(2):
    tetro7=rotation(tetro7)
    for i in range(n-len(tetro7)+1):
        for j in range(m-len(tetro7[0])+1):
            tot=0

            for x in range(len(tetro7)):
                for y in range(len(tetro7[0])):
                    if tetro7[x][y]==1:
                        tot+=mop[i+x][j+y]
                        maxi=max(maxi,tot)  
print(maxi)            

# tetro4=rotation(tetro4)
# print(tetro4)
# tetro4=rotation(tetro4)
# print(tetro4)
# for i in range(3):
#     print(tetro4[i])










