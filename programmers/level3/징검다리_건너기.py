def solution(stones, k):
    answer = max(stones)
    
    s, e = 1, max(stones)
    while s <= e:
        mid = (s+e)//2
        t = 0
        for stone in stones:
            if stone - mid <= 0:
                t += 1
            else:
                t = 0
            if t >= k:
                break
        if t < k:
            s = mid + 1
        else:
            answer = mid
            e = mid - 1
    return answer