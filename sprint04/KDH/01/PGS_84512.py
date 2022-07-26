from itertools import product


def solution(word):
    answer = 0
    words = []
    c = ['A', 'E', 'I', 'O', 'U']

    for i in range(5):
        res = list(product(c, repeat=i+1))
        for r in res:
            words.append(''.join(r))

    words.sort()
    answer = words.index(word)+1
    return answer
