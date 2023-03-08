from itertools import permutations
from itertools import combinations
import sys

def check_satisfy_cond(tup):

    count = 0
    count_b = 0

    for i in range(len(tup)):
        if tup[i] in "aieou":
            count += 1
        else:
            count_b += 1
    
    if count > 0 and count_b > 1:
        return True
    else:
        return False

if __name__ == "__main__":
    
    L, C = map(int, sys.stdin.readline().split())
    lst = sorted(sys.stdin.readline().split())

    answer = []

    llst = list(combinations(lst, L))

    for i in (llst):
        if check_satisfy_cond(i):
            answer.append(''.join(i))

    for i in (answer):
        print(i)
