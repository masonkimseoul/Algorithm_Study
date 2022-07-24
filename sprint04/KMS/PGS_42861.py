def solution(n, costs):  #kruskal 알고리즘
    costs.sort(key=lambda x:x[2])  #비용 오름차순으로 정렬
    answer = 0
    routes=set([costs[0][0]])
    while len(routes)<n:
        for idx,cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0],cost[1]])
                answer+=cost[2]
                del costs[idx]
                break
    return answer