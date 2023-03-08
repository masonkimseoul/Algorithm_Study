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
    for departure, arrival in tickets:
        graph[departure].append(arrival)
    for departure, arrival in graph.items():
        graph[departure].sort()

    dfs("ICN")

    return answer[::-1]
