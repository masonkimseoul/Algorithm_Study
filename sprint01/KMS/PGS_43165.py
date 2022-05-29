def solution(numbers, target):
    answer = 0
    tree = [0]
    for i in range(len(numbers)):
        list = []
        for j in range(len(tree)):
            list.append(tree[j] - numbers[i])
            list.append(tree[j] + numbers[i])
        tree = list
    
    answer = tree.count(target)
    
    return answer