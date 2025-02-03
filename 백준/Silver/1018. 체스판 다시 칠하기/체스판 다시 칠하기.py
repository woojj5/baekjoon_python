n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
res = []
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] == 'W':
                        cnt1+=1
                    if board[a][b] == 'B':
                        cnt2+=1
                else:
                    if board[a][b] == 'B':
                        cnt1+=1
                    if board[a][b] == 'W':
                        cnt2+=1
        res.append(cnt1)
        res.append(cnt2)
print(min(res))