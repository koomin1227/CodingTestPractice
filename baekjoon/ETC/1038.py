from itertools import combinations

n = int(input())

down_numbers = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))
        down_numbers.append(int(num))
down_numbers.sort()
if n >= len(down_numbers):
	print(-1)
else:
	print(down_numbers[n])
