import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
field =  [list(map(int, input().split())) for i in range(n)]
ans = 1e9
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
    if use > tak + b:
        continue
    count = tak * 2 + use

    if count <= ans:
        ans = count
        glevl = i
print(ans, glevl)
