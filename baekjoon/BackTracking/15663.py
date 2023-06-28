from itertools import permutations

n,m = map(int,input().split())
num = list(map(int,input().split()))
comb = set(permutations(num, m))
comb = list(comb)
comb.sort()
for i in comb:
    for j in i:
        print(j,end=' ')
    print()