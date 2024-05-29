a = list(map(int, input().split()))
n = min(a)
cnt = 0
while cnt < 3:
    cnt = 0
    for i in a:
        if n % i == 0:
            cnt +=1
        if cnt == 3:
            print(n)
            break
    n +=1