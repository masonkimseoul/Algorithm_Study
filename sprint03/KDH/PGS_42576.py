# 01.
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for p, c in zip(participant, completion):
#         if p != c:
#             return p
#     return participant[-1]

# 02. hash
def solution(participant, completion):
    hash_table = {}
    hash_value = 0
    for p in participant:
        hash_table[hash(p)] = p
        hash_value += hash(p)
    for c in completion:
        hash_value -= hash(c)

    answer = hash_table[hash_value]
    return answer
