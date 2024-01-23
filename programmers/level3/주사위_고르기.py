from itertools import combinations
def solution(dice):
    answer = []
    max_winning = 0
    n = len(dice)
    # a가 가질 수 있는 주사위 조합을 구하기
    nums = [i for i in range(n)]
    adice = list(combinations(nums,n//2))
    # 주사위를 굴려서 나올 수 있는 합 구하기
    def dfs(depth, nums, total, now):
        if depth == n //2:
            total.append(now)
            return
        for i in range(6):
            now += dice[nums[depth]][i]
            dfs(depth + 1, nums, total, now)
            now -= dice[nums[depth]][i]
        return total
    # a가 이기는 경우의 수를 찾기
    for i in range(len(adice)):
        bdice = []
        for j in nums:
            if j not in adice[i]:
                bdice.append(j)
        a_result = dfs(0, adice[i], [], 0)
        b_result = dfs(0, bdice, [], 0)
        a_result.sort()
        b_result.sort()

        a,b,tot = 0,0,0
        while a < len(a_result):
            if b < len(b_result) and a_result[a] > b_result[b]:
                b += 1
            else:
                tot += b
                a += 1
        if tot > max_winning:
            max_winning = tot
            answer = list(adice[i])

    for i in range(len(answer)):
        answer[i] += 1
    answer.sort()
    return answer