class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


L = list(map(str, input().strip()))
N = int(input())
head = Node(L[0])
pnode = head


def PrintList():
    pnode = head
    while pnode != tail:
        print(pnode.data, end='')
        pnode = pnode.next
    print()


for i in L[1:]:
    t = Node(i)
    t.prev = pnode
    pnode.next = t
    pnode = t
tail = Node(0)
pnode.next = tail
tail.prev = pnode
pnode = tail

for i in range(N):
    A = list(map(str, input().split()))
    if A[0] == 'P':
        t = Node(A[1])
        if pnode == head:
            t.next = pnode
            pnode.prev = t
            head = t
        else:
            t.next = pnode
            t.prev = pnode.prev
            pnode.prev.next = t
            pnode.prev = t
    elif A[0] == 'L':
        if pnode == head:
            continue
        else:
            pnode = pnode.prev
    elif A[0] == 'D':
        if pnode != tail:
            pnode = pnode.next
    else:
        if pnode == head:
            continue
        else:
            if pnode == head.next:
                deletenode = pnode.prev
                pnode.prev = None
                head = pnode
                deletenode = None
            else:
                deletenode = pnode.prev
                pnode.prev = deletenode.prev
                pnode.prev.next = deletenode.next
                deletenode = None
PrintList()


# dmih
# 11
# B
# B
# P x
# L
# B
# B
# B
# P y
# D
# D
# P z

# abc
# 9
# L
# L
# L
# L
# L
# P x
# L
# B
# P y
