def solution(sizes):
    answer = 0
    row = []
    col = []
    for i in sizes:
        row.append(max(i))
        col.append(min(i))
    answer = max(row) * max(col)
    return answer