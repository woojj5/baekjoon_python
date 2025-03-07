from collections import deque
t  = int(input())
for _ in range(t):
    str = list(input())
    n = int(input())
    arr = input().strip()[1:-1].split(",")
    q = deque(arr)
    cnt = 0
    chk = 0
    if n == 0:
        q = deque()
    for s in str:
        if s == 'R':
            cnt+=1
        else:
            if not q:
                print('error')
                chk = 1
                break
            else:
                if cnt %2:
                    q.pop()
                else:
                    q.popleft()
    if not chk:
        if cnt % 2:
            q.reverse()
        print('[' + ','.join(q) + ']')