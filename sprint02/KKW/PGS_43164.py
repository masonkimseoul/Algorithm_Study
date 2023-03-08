def solution(tickets):
    answer = []
    airline = {}
    for t in tickets:
        if t[0] in airline:
            airline[t[0]].append(t[1])
        else:
            airline[t[0]] = [t[1]]

    for a in airline.keys():
        airline[a].sort(reverse=True)

    start = ["ICN"]
    while start:
        target = start[-1]
        if target not in airline or len(airline[target]) == 0:
            answer.append(start.pop())
        else:
            start.append(airline[target].pop())

    return answer[::-1]