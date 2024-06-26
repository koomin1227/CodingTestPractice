n,m = map(int, input().split())

sausage_len = m
total_len = sausage_len * n
sausage_len_person = total_len / m
count = 0
tot_len = 0
for i in range(m):
    tot_len += sausage_len_person
    if tot_len % sausage_len != 0:
        count += 1

print(count)



