import sys
basis=list(sys.stdin.readline().rstrip())
temp=[]
N=int(sys.stdin.readline())

for _ in range(N):
    command=sys.stdin.readline().split()
    if command[0]=='P':
        basis.append(command[1])
    elif command[0]=='L' and len(basis)!=0:
        temp.append(basis.pop())
    elif command[0]=='D' and len(temp)!=0:
        basis.append(temp.pop())
    elif command[0]=='B' and len(basis)!=0:
        basis.pop()
print("".join(basis+list(reversed(temp))))