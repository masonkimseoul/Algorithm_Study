def dfs(idx, dic, visited):
    if idx in visited:
        return
    visited.append(idx)

    for i in dic[idx]:
        dfs(i, dic, visited)
        
# def dfs(idx, dic, visited):
#     for i in dic[idx]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic, visited)

def solution(n, computers):
    answer = 0
    
    dic = dict()
    for i in range(n):
        dic[i + 1] = []
    for idx, i in enumerate(computers, start=1):
        for idx_, j in enumerate(i, start=1):
            if idx == idx_:
                continue
            if j == 1:
                dic[idx].append(idx_)
                
    visited = []
    
    for i in range(1, n + 1):
        if i not in visited:
            answer += 1
            dfs(i, dic, visited)
    
    return answer