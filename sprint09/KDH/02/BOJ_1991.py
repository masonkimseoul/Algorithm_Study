import sys
input = sys.stdin.readline

N = int(input().rstrip())
tree = dict()
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]


def preorder(n):
    if n != ".":
        print(n, end = "")
        preorder(tree[n].left)
        preorder(tree[n].right)

def inorder(n):
    if n != ".":
        preorder(tree[n].left)
        print(n, end = "")
        preorder(tree[n].right)

def postorder(n):
    if n != ".":
        preorder(tree[n].left)
        preorder(tree[n].right)
        print(n, end = "")

preorder('A')
print()
inorder('A')
print()
postorder('A')

