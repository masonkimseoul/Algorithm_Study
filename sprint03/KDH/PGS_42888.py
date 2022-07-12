# 오픈채팅방
from collections import defaultdict


def solution(record):
    answer = []
    name_dic = defaultdict(list)
    action_dic = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
    res = []

    for i in range(len(record)):
        record[i] = record[i].split(" ")
        if record[i][0] == "Enter":
            res.append(["Enter", record[i][1]])
            name_dic[record[i][1]] = record[i][2]
        elif record[i][0] == "Leave":
            res.append(["Leave", record[i][1]])
        else:
            name_dic[record[i][1]] = record[i][2]

    for i in range(len(res)):
        answer.append(name_dic[res[i][1]]+"님이 " + action_dic[res[i][0]])

    return answer
