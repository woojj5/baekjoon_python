t =  10
for times in range(1, t+1):
    n = int(input())
    lista = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        mx = max(lista[i-2: i] + lista[i+1: i+3])
        if lista[i] > mx:
            ans += lista[i] - mx
    print(f'#{times} {ans}')
