n = int(input())
files = list(map(int,input().split()))
# files = [100, 99]
files.sort(reverse=True)

def binary_search(i, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        size = files[mid]
        if size < target:
            r = mid - 1
        else:
            l = mid + 1
    return (l - i) - 1 



total = 0
for i in range(n):
    l = i + 1
    total += binary_search(i, l, n - 1, files[i] * 0.9)
print(total)
# print(files)




# 11 8 6 6 5 5 4