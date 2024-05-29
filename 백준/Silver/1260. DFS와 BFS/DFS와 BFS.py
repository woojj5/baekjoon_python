from collections import deque

def dfs(s):
    visit[s] = 1
    print(s+1, end = " ")
    for i in range(v):
        if arr[s][i] == 1 and visit[i] == 0:
            dfs(i)

def bfs(s):
    q = deque()
    q.append(s)
    visit2[s] = 1
    while q:
        c = q.popleft()
        print(c+1, end = " ")
        for i in range(v):
            if  visit2[i] == 0 and arr[c][i] == 1:
                q.append(i) 
                visit2[i] = 1   

v, n, s = map(int, input().split())
arr = [[0] * v for i in range(v)]
#print(arr)
visit = [0] * v
visit2 = [0] * v

for t in range(n):
    x,y =  map(int, input().split())
    arr[x-1][y-1] = arr[y-1][x-1] =  1
dfs(s-1)
print()
bfs(s-1)