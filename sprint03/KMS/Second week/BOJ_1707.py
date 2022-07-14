N = int(input())

for k in range(N):
    answer = 0
    graph = {}
    v, e = map(int, input().split())
    for _ in range(e):
        x, y = map(int, input().split())
        if x not in graph.keys():
            graph[x] = set([y])
        else:
            graph[x].add(y)
        if y not in graph.keys():
            graph[y] = set([x])
        else:
            graph[y].add(x)
    

    
    visit = [0] * (v+1)
    def dfs(vertex,team):
        visit[vertex] = team
        for i in graph[vertex]:
            if visit[i] == 0:
                # print(i)
                if(team == 'A'):
                    dfs(i,'B')
                else:
                    dfs(i,'A')
    visit1 = [False] * (v+1)
    def check(vertex,team):
        global answer
        visit1[vertex] = True
        tmp = visit[vertex]
        if visit[vertex] == team:
            answer = 1
        for i in graph[vertex]:
            if not visit1[i]:
                check(i,tmp)
    for i in range(1,v):
        answer = 0
        # print('________')
        check(i,' ')
    # print(visit)
    # visit1 = [0] * (v+1)
    
    # def check(vertex,team):
    #     global answer
    #     visit1[vertex] = 1
    #     tmp = visit[vertex]
    #     print(tmp, team)
    #     if tmp == team:
    #         answer = 1
    #     for i in graph[vertex]:
    #         if not visit1[i]:
    #             check(i,tmp)
                
    # check(1,' ')
    
    if answer:
        print('NO')
    else:
        print('YES')
    




    # for i in graph:
    #     print(i)
    

    
    # print(group)


