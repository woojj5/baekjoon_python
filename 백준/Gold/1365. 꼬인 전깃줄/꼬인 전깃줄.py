import bisect
n = int(input())
lisa  = list(map(int, input().split()))
stack = []
for i in lisa:
    if not stack or stack[-1] < i:
        stack.append(i)
        continue
    loc = bisect.bisect_left(stack, i)
    stack[loc] = i
print(n - len(stack))