from itertools import combinations
def solution (nums) :
    answer = -1
    # cnt = [0]  
    def is_prime(select):
        i=2
        while i*i<=select:
            if select % i == 0:
                return 0
            i=i+1
        return 1
    # def dfs(depth, visited, select, nums,prev):
    #     if depth == 3:
    #         if is_prime(select) == 1:
    #             cnt[0] +=1
    #         return
    #     for i in range(prev+1,len (nums)):
    #         if visited[i] == 0:
    #             visited[i] = 1
    #             select += nums[i]
    #             dfs (depth+1, visited, select, nums,i)
    #             visited[i] = 0
    #             select -= nums[i]
    # visited=[0]*(len (nums))
    # dfs(0, visited,0, nums,-1)
    com=list(combinations(nums,3))
    cnt=0
    for i in com:
        if is_prime(sum(i)) == 1:
            cnt+=1
    answer = cnt
    return answer
print(solution([1,2,7,6,4]))