#https://www.acmicpc.net/problem/1202
# 알고리즘 아이디어 : 배낭의 무게를 오름차순으로 정렬하고 보석은 무게를 기준으로 오름차순 정렬을 해둔다. 
# 배낭 하나를 뽑아 그 배낭에 넣을 보석을 고를때 보석 리스트에서 현재 배낭 보다 무게가 작거나 같은 보석을 전부 뽑아 가치 중점 힙에 넣는다
# 힙에서 가치가 가장 큰 원소를 뽑으면 그것이 그 배낭의 최적해이다. 가치중점힙은 초기화 시키지 않는다. 크기가 작은 것 결정후에 크기가 큰걸 볼떄 이미 가치중점에
# 들어 있는 원소들은 크기가 더 큰 배낭에 들어갈수 있는 보석들이기 때문 
from sys import stdin
import heapq
input=stdin.readline
n,k=map(int,input().split())
gem_weight=[]
bag=[]
for i in range(n):#무게순으로 힙에 삽입
    m,v=map(int,input().split())
    heapq.heappush(gem_weight,(m,v))
for i in range(k):
    bag.append(int(input()))
bag.sort()
tot=0
gem_value=[]
for i in bag:
    while gem_weight and gem_weight[0][0]<=i:#현재 가방보다 무게가 작거나 같은 모든 가방으로 꺼내어 다른 힙에 담는다
        heapq.heappush(gem_value
    ,heapq.heappop(gem_weight)[1]*-1)#가치를 기준으로 힙에 삽입
    if gem_value:##가치 기준 힙에 원소가 있다면 그걸 뽑기
        tot-=heapq.heappop(gem_value
    )
    elif not gem_weight:#가치기준 힙에도 원소 없고 보석 힙에도 없으면 끝낸다 더 이상 할게 없다.
        break
print(tot)