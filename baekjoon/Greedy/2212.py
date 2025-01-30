n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

sensors.sort()
differ = []
for i in range(n - 1):
    differ.append(sensors[i + 1] - sensors[i])
differ.sort()

print(sum(differ[:n - k]))