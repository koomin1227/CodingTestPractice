def solution(n, times):
    answer = 0
    left = 0
    person = n // len(times)
    if n % len(times) != 0:
        person += 1
    right = max(times) * person
    while left < right:
        mid = (left + right) // 2
        throughput = 0
        for time in times:
            throughput += mid // time
        print(mid,throughput)
        if throughput >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer