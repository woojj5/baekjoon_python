target = int(input())
init = 0

def dfs(val, cnt):
    if val >= target:
        print(cnt)
        return
    if val == 0:
        dfs(val+1, cnt+1)
    else:
        dfs(val*2, cnt+1)

dfs(0,0)