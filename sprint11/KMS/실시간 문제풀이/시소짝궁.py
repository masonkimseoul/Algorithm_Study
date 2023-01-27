def findrange(W, l, maxindex, goal):
    start = l
    end = maxindex
    while start <= end:
        mid = (start + end) // 2
        if W[mid] > goal:
            end = mid - 1
        else:
            start = mid + 1
    return start


def solution(weights):
    answer = 0
    weights.sort()
    size = len(weights)
    for idx in range(size-1):
        if idx > 0 and weights[idx] == weights[idx-1]:
            prev -= 1
            answer += prev
            continue
        end = findrange(weights, idx, size-1, weights[idx] * 2)
        data = weights[idx]
        prev = 0
        for i in range(idx+1, end):
            if data * 2 == weights[i] or data * 3/2 == weights[i] or data == weights[i] or data * 4/3 == weights[i]:
                answer += 1
                prev += 1
    return answer
