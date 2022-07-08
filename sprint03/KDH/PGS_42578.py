def solution(clothes):
    answer = 1
    clothes_ = {}

    for name, kind in clothes:
        if kind in clothes_.keys():
            clothes_[kind].append(name)
        else:
            clothes_[kind] = [name]

    for key in clothes_.keys():
        answer *= len(clothes_[key])+1
    answer -= 1

    return answer
