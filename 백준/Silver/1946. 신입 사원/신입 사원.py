t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for k in range(n):
        a,b = map(int, input().split())
        arr.append((a,b))
    arr.sort()
    stack = []
    for i in range(n):
        if i == 0:
            stack.append(arr[i])
        else:
            if stack[-1][1] >= arr[i][1]:
                stack.append(arr[i])
            else:
                pass
    print(len(stack))