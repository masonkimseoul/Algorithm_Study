
global_lst = []

def dfs(city, dic, checked):
    
    global global_lst

    if city not in checked or not dic[city]:
        global_lst.append(city)
        return
    
    global_lst.append(city)
    
    new_city = dic[city].pop(0)
    dfs(new_city, dic, checked)

def solution(tickets):
    answer = []
    dic = dict()
    checked = []
    
    for i in tickets:
        if i[0] not in checked:
            dic[i[0]] = []
            checked.append(i[0])
        dic[i[0]].append(i[1])

    for i in dic:
        dic[i].sort()
        
    # print(dic)
    
    global global_lst
    
    dfs("ICN", dic, checked)

    answer = global_lst
    
    return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])==["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
# print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]) == ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]))
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]) == ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"])
