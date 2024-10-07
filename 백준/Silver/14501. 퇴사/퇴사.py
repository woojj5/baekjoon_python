n = int(input())
lista = [list(map(int, input().split())) for i in range(n)]
def sol(i):
    if i >= n:
        return 0
    ret = 0
    if i + lista[i][0] <=  n:
        ret = sol(i+lista[i][0]) + lista[i][1] 
    ret = max(ret, sol(i+1))
    return ret
print(sol(0))