n = int(input())
op = list(input().split())
ch = 0
res = []

def operator(x,y,op):
    if op == '<':
        if x> y:
            return False
    else:
        if x < y:
            return False
    return True

res = []
ans = []
def dfs(level):
    global res
    if level == n+1:
        ans.append(''.join(map(str, res)))
        return
    for i in range(10):
        if i not in res:
            if level == 0 or operator(res[level-1], i, op[level-1]):
                res.append(i)
                dfs(level+1)
                res.pop()
dfs(0)
print(ans[-1])
print(ans[0])