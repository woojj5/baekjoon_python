arr = input()
stack = []
tmp = 1
ans = 0
for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
        tmp*=2

    elif  arr[i] == "[":
        stack.append(arr[i])
        tmp*=3

    elif arr[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break

        if arr[i-1] == "(":
            ans+=tmp

        tmp//=2
        stack.pop() 
    
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if arr[i-1] == "[":
            ans+=tmp
        tmp//=3
        stack.pop() 

if stack:
    print(0)
else:
    print(ans)