import sys
input = sys.stdin.readline

N = input().strip()

stack = ''

count = 0
result = 0
for i in N:
  if '0' <= i <= '9':
    stack += i
  else:
    if i == '-':
      if count ==1:
        result -= int(stack)
      else:
        result += int(stack)
        count = 1
      stack =''
    else:
      if count ==1:
        result -= int(stack)
      else:
        result += int(stack)
      stack=''
if count == 1:
  result -= int(stack)
else:
  result += int(stack)
print(result)
