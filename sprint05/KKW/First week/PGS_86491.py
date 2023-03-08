def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    width=[]
    length=[]
    for i in range(len(sizes)):
        width.append(sizes[i][0])
        length.append((sizes[i][1]))
    return max(width)*max(length)