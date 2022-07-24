def solution(n, costs):
    answer = 0

    costs.sort(key = lambda x : x[2])
    visited = set([costs[0][0]])
    cnt = 0
    
    while cnt < n - 1:
        for i in costs:
            A, B, cost = i
            if (A in visited and B in visited):
                continue
            if (A in visited or B in visited):
                visited.add(A)
                visited.add(B)
                answer += cost
                cnt += 1
                
                break

    return answer

