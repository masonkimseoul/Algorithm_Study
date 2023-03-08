def solution(k, dungeons) :
    return search(k, dungeons, 0)


def search(k, dungeons, cnt) :
    cnt_list = [cnt]

    for i in range(len(dungeons)) :
        if dungeons[i][0] <= k :
            temp_list = dungeons.copy()
            del temp_list[i]
            cnt_list.append(search(k - dungeons[i][1], temp_list, cnt + 1))

    
    return max(cnt_list)