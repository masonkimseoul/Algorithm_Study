from itertools import combinations

if __name__ == "__main__":

    count = 0

    n, s = map(int, input().split());
    lst = list(map(int, input().split()));

    for i in range(1, len(lst) + 1):
        llst = list(combinations(lst, i))
        for j in llst:
            if sum(j) == s:
                count += 1

    print(count)
