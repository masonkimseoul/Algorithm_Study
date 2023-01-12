def solution(n, m, x, y, r, c, k):
    answer = ''
    graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
    route = []
    def DFS(x,y,troute,cnt):
        if cnt==k and x == r and y ==c:
            route.append(troute)
        if cnt >= k:
            return
        remain = k - cnt + 1
        short = abs(x-r) + abs(y-c)
        if remain < short:
            return
        nx = [1,0,0,-1]
        ny = [0,-1,1,0]
        t = ['d','l','r','u']
        for i in range(4):
            dx = nx[i] + x
            dy = ny[i] + y
            if 1<= dx <= n and 1<= dy <= m:
                if route:
                    return
                else:
                    DFS(dx,dy,troute + t[i],cnt+1)
    DFS(x,y,'',0)
    route.sort()
    if route:
        answer = route[0]
    else:
        answer = 'impossible'
    return answer