import sys
sys.setrecursionlimit(10**4)
N = int(input())

for _ in range(N):
    answer = 0
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]  # 빈 그래프 생성
    for _ in range(e):
        a, b = map(int, input().split())
        # if b in graph[a]:
        #     continue
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    visit = [0] * (v+1)
    def dfs(vertex,team,pre):        
        global answer
        visit[vertex] = team
        # print(vertex , ' : ', team)
        for i in graph[vertex]:
            # print('e = ', i)
            if visit[i] == 0:
                if(team == 'A'):
                    dfs(i,'B',vertex)
                else:
                    dfs(i,'A',vertex)
        return
    for i in range(1,len(graph)):
        if visit[i] == 0:
            dfs(i,'A', 0)
            # print('______')
            
    # print(graph)
    # print(visit)
    for i in range(1,len(graph)):
        # print('i = ', i)
        for j in graph[i]:
            # print(j)
            if visit[i] == visit[j]:
                answer = 1
    
    
    if answer:
        print('NO')
    else:
        print('YES')
    