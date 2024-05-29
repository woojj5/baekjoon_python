def cal(n, p):
    result = 0
    for i in str(n):
        result += int(i) ** p
    return result

def dfs(n, p, count, visit):
    if visit[n] != 0:
        return visit[n] - 1
    visit[n] = count
    next = cal(n,p)
    count +=1
    return dfs(next, p, count, visit)

n, p = map(int, input().split())
count = 1
visit = [0]*(4*9**5 + 1)
print(dfs(n,p, count, visit))