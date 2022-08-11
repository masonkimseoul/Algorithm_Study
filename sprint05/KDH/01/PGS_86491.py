def solution(sizes):
    max1, max2 = -1, -1

    for size in sizes:
        size.sort()

        max1 = max(max1, size[1])
        max2 = max(max2, size[0])

    return max1*max2
