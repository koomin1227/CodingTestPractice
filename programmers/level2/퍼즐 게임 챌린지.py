def calc_time(level, diffs, times):
    total_time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            total_time += times[i]
        else:
            total_time += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
    return total_time
            
def solution(diffs, times, limit):
    answer = max(diffs)
    l = 1
    r = max(diffs)
    while l < r:
        mid = (l + r) // 2
        total_time = calc_time(mid, diffs, times)
        print(total_time)
        if total_time <= limit:
            r = mid
            answer = r
        else:
            l = mid + 1
    # answer = l
    return answer


print(solution([1, 5, 3], [2, 4, 7], 30))