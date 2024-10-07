import sys

n,m,b = map(int, sys.stdin.readline().split())
field =  [list(map(int, sys.stdin.readline().split())) for i in range(n)]
ans = sys.maxsize
glevl = 0
for i in range(257):
    use = 0
    tak = 0
    for x in range(n):
        for y in range(m):
            if field[x][y] >i:
                tak+= field[x][y]  - i
            else:   
                use+= i - field[x][y]
    if use <= tak + b:
        if use + tak * 2 <= ans:
            ans = use + tak*2 
            glevl = i
print(ans, glevl)
    