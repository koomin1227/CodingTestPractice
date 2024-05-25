n , x = map(int, input().split())
nums = list(map(int,input().split()))

sums = []
total = sum(nums[:x])
sums.append(total)
l = 0
for i in range(x, n):
    total -= nums[l]
    total += nums[i]
    l += 1
    sums.append(total)

max_visitor = max(sums)
if max_visitor == 0:
    print('SAD')
else:
    duration = 0
    for i in sums:
        if i == max_visitor:
            duration += 1

    print(max_visitor)
    print(duration)