n, k = map(int, input().split())
drink = []

for i in range(n):
    drink.append(int(input()))

l = 1
r = sum(drink) // k + 1

while l < r:
    mid = (l + r) // 2
    total_amount = 0
    total_count = 0
    for d in drink:
        total_count += (d // mid)
        total_amount += mid * (d // mid)

    if total_count < k:
        r = mid
    elif total_count >= k:
        l = mid + 1

print(l - 1)



