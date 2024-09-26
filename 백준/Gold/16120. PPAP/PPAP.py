st = input()
stack  = []
for i in st:
    stack.append(i)
    if ''.join(stack[-4:]) == "PPAP":
        for i in range(4):
            stack.pop()
        stack.append("P")
if ''.join(stack) == "P":
    print("PPAP")
else:
    print("NP")