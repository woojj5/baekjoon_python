S = input()
T = input()
ans = 0
def dfs(t):
    global ans
    if t == S:
        ans = 1
        return 
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])
dfs(T)
print(ans)
