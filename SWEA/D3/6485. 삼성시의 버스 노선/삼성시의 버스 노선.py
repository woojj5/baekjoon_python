t = int(input())
for timestamp in range(t):
    n = int(input())
    arr = [0] * 5001
    for i in range(n):
        x,y = map(int, input().split())
        for j in range(x, y+1):
            arr[j] +=1
    
    P = int(input())
    sol = []
    for i in range(P):
        sol.append(arr[int(input())])
    print(f'#{timestamp+1}', *sol)