answer = 0
def dfs(k, dungeons, cnt, visited):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if visited[i] == 0 and k>= dungeons[i][0]:
            visited[i] = 1
            dfs(k-dungeons[i][1], dungeons, cnt+1, visited)
            visited[i] = 0
    
def solution(k, dungeons):
    global answer
    visited = [0] * len(dungeons)
    dfs(k, dungeons, 0, visited)
    return answer