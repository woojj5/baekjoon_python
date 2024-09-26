st = list(input())
bomb = list(input())
bb = len(bomb)
ans = "FRULA"

stack = []
for i in st:
    stack.append(i)
    if stack[-bb:] == bomb:
        for _ in range(bb):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))