from collections import deque
n = int(input())
Q = deque([n])
visit = [0] *(n+1)
while Q:
    c = Q.popleft()
    if c == 1:
        break
    if c%3 == 0 and visit[c//3] == 0:
        Q.append(c//3) 
        visit[c//3] = visit[c] +1
    
    if c%2 == 0 and visit[c//2] == 0:
        Q.append(c//2) 
        visit[c//2] = visit[c] +1

    if visit[c-1] == 0:
        Q.append(c-1) 
        visit[c-1] = visit[c] +1

print(visit[1])
            
