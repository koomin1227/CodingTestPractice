import sys
sys.setrecursionlimit(10**6)
def solution(n, m, x, y, r, c, k):
    answer = ''
    direction = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    dist = abs(x - r) + abs(y - c)
    if dist > k or abs(dist - k) % 2 == 1:
        return 'impossible'
    def dfs(x, y, depth, res):
        if depth == k:
            if x == r and y == c:
                return res
            else:
                return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= m:
                dist = abs(nx - r) + abs(ny - c)
                if dist > k - depth:
                    continue
                res.append(direction[i])
                ans = dfs(nx, ny, depth + 1, res)
                if ans != None:
                    return ans
                res.pop()

    answer = ''.join(dfs(x,y,0,[]))
    return answer