from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    plays_by_genre = {}

    for idx, [g, p] in enumerate(zip(genres, plays)):
        dic[g].append((idx, p))
        if g in plays_by_genre:
            plays_by_genre[g] += p
        else:
            plays_by_genre[g] = p

    plays_by_genre = sorted(plays_by_genre.items(),
                            key=lambda x: x[1], reverse=True)
    for g in plays_by_genre:
        tmp = sorted(dic[g[0]], key=lambda x: x[1], reverse=True)
        cnt = min(2, len(tmp))
        for i in range(cnt):
            answer.append(tmp[i][0])

    return answer
