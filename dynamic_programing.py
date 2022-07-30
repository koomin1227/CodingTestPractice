from sys import stdin
from itertools import combinations
read=stdin.readline
n,k=map(int,read().split())
c=list(combinations(range(n),k))
print(len(c))






















    
