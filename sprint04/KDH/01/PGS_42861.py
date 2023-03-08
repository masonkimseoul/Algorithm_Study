def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    print(costs)
    visited = [0] * n

    idx = 0
    while sum(visited) != n:
        is1, is2, cost = costs[idx][0], costs[idx][1], costs[idx][2]

        if (sum(visited) == 0) or (visited[is1]+visited[is2] == 1):
            answer += cost
            visited[is1] = 1
            visited[is2] = 1
            costs.pop(idx)
            idx = 0
        else:
            idx += 1

        if sum(visited) == n:
            return answer
