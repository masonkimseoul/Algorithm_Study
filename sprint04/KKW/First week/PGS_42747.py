def solution(citations):
    for i, val in enumerate(sorted(citations, reverse=True)):
        if i>=val:
            return i
    return len(citations)
