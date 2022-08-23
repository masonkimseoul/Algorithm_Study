import sys

T=int(sys.stdin.readline())
sentence=[]
letters=[]
letters_list=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(26):
    letters.append(0)

for i in range(T):
    tmp=sys.stdin.readline().rstrip()
    sentence.append(list(tmp))
    cnt=1
    for j in range(len(sentence[i])-1,-1,-1):
        letters[letters_list.index(sentence[i][j])]+=cnt
        cnt*=10

letters.sort(reverse=True)
cnt=9
i=0

while cnt>=0:
    letters[i]*=cnt
    i+=1
    cnt-=1
print(sum(letters))