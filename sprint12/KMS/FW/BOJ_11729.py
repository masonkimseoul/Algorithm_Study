N = int(input())


def hanoi(N, start, middle, dest):
    if N == 1:
        return 1
    result = 0

    result += hanoi(N-1, start, dest, middle)
    result += hanoi(1, start, middle, dest)
    result += hanoi(N-1, middle, start, dest)
    return result


def hanoi_print(N, start, middle, dest):
    if N == 1:
        print(start, dest)
        return 1
    result = 0

    result += hanoi_print(N-1, start, dest, middle)
    result += hanoi_print(1, start, middle, dest)
    result += hanoi_print(N-1, middle, start, dest)
    return result


print(hanoi(N, 1, 2, 3))
hanoi_print(N, 1, 2, 3)
