import sys
input = sys.stdin.readline().strip()
n = input
size = len(n)
lazer = []
stick = []
result = []
i = 0
while True:
  if n[i] == '(' and n[i+1] == ')':
    lazer.append(i)
    i+=2
    continue
  elif n[i] == '(':
    stick.append(i)
  elif n[i] == ')':
    t = stick.pop()
    result.append((t,i))
  i+=1
  if i == size:
    break

count = 0

for i in result:
  start, end = i
  count +=1
  for j in lazer:
    if start <= j <= end:
      count+=1
print(count)