from collections import defaultdict
answer = []
graph = defaultdict(list)


def dfs(v):
    while graph[v]:
        dfs(graph[v].pop(0))
    if not graph[v]:
        answer.append(v)
        return


def solution(tickets):
    for s, e in tickets:
        graph[s].append(e)
    for s, e in graph.items():
        graph[s].sort()

    dfs("ICN")

    return answer[::-1]
