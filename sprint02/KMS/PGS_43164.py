def solution(tickets):
    res = []
    answer=[]
    def DFS(start,ticket_list,res):
        res.append(start)
        if len(ticket_list)==1:
            res.append(ticket_list[0][1])
            answer.append(res)
        else:
            for t in ticket_list:
                if start==t[0]:
                    copy_tList=ticket_list.copy()
                    copy_tList.remove(t)
                    DFS(t[1],copy_tList,res.copy())
    DFS('ICN',tickets,res)       
    return min(answer)