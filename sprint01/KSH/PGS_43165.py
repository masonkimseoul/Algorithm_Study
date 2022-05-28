'''
    첫 번째 방법 (BFS)
'''

def solution(numbers, target):
    answer = 0

    lst = [0]
    for i in numbers:
        llst = []        
        for j in lst:
            llst.append(j - i)
            llst.append(j + i)
        lst = llst
    
    answer = lst.count(target)
    
    return answer


'''
    두 번째 방법 (DFS)
'''

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth + 1)
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    
    return answer




