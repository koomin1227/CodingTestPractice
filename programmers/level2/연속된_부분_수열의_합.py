def solution(sequence, k):
    answer = []
    length = 1000000
    
    l = 0
    r = 0
    s_sum = sequence[0]
    while r < len(sequence):
        if s_sum < k:
            r += 1
            if r < len(sequence):
                s_sum += sequence[r]
        elif s_sum > k:
            s_sum -= sequence[l]
            l += 1
        else:
            if length > r - l:
                length = r - l
                answer = [l,r]
            r += 1
            if r < len(sequence):
                s_sum += sequence[r]
    return answer