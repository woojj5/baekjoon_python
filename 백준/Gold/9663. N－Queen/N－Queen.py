n = int(input())
node = [0] * n
def promise(x):
    for i in range(x):
        if node[i] == node[x] or abs(i-x) == abs(node[i] - node[x]):
            return False
    return True
cnt = 0
def nqueens(x):
    global cnt
    if x == n:
        cnt +=1
        return
    for i in range(n):
        node[x] = i
        if promise(x):
            nqueens(x+1)
nqueens(0)
print(cnt)