import sys
input = sys.stdin.readline

n = int(input())
graph={}
for i in range(n):
  name, left, right = input().split()
  graph[name] = (left,right)

def preorder(root):
  if root == '.':
    return
  print(root, end='')
  preorder(graph[root][0])
  preorder(graph[root][1])

def inorder(root):
  if root == '.':
    return
  inorder(graph[root][0])
  print(root, end='')
  inorder(graph[root][1])
def postorder(root):
  if root == '.':
    return
  postorder(graph[root][0])
  postorder(graph[root][1])
  print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')