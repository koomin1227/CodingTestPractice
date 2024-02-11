def solution(n, k):
    def is_prime(nums):
        num = 0
        for i in nums:
            num = num * 10 + i
        if num == 0 or num == 1:
            return False
        tot = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                tot += 1
        if tot == 1:
            return True
        else:
            return False
        
        
    answer = 0
    nums = []
    while n != 0:
        nums.append(n % k)
        n = n // k
    nums.reverse()

    for i in range(len(nums)):
        if nums[i] != 0:
            continue
        j = i - 1
        while j > 0 and nums[j - 1] != 0 and nums[j] != 0:
            j -= 1
        if is_prime(nums[j:i]):
            answer+=1
        
    i += 1
    j = i - 1
    while j > 0 and nums[j - 1] != 0 and nums[j] != 0:
        j -= 1
    if is_prime(nums[j:i]):
        answer+=1

    return answer