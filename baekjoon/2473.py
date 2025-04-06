n = int(input())

arr = list(map(int, input().split()))
arr.sort()

minimum = [3000000000, 0, 0, 0]

for fix in range(n - 2):
    l = fix + 1
    r = n - 1
    while l < r:
        cur_sum = arr[fix] + arr[l] + arr[r]
        if minimum[0] > abs(cur_sum):
            minimum[0] = abs(cur_sum)
            minimum[1] = arr[fix]
            minimum[2] = arr[l]
            minimum[3] = arr[r]
            
        if cur_sum < 0:
            l += 1
        else:
            r -= 1

answer = minimum[1:]
answer.sort()
for num in answer:
    print(num, end = ' ')