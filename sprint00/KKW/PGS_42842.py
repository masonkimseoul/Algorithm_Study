def solution(brown, yellow):
    answer=[]
    col=1
    row=yellow//col
    brown-=4

    while(col<=row):
        if col*2+row*2==brown:
            answer.append(row+2)
            answer.append(col+2)
            return answer
        col+=1
        if yellow%col==0:
            row=yellow//col
        else:
            while(yellow%col!=0):
                col+=1
                row=yellow//col

#yellow%col==0인지 확인 필