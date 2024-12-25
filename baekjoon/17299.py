n = int(input())
a = list(map(int, input().split()))

num_count = {}

for i in range(n):
    if a[i] not in num_count:
        num_count[a[i]] = 0
    num_count[a[i]] += 1

result = [-1] * n
stack = []
for i in range(n):
    while stack and num_count[a[stack[-1]]] < num_count[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)

for i in result:
    print(i, end=" ")
# print(result)