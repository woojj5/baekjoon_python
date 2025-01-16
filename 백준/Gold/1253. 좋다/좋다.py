n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
#부분합과 동일한 값을 찾는 문제이기 때문에, 이는 투포인터를 이용해서 풀어야 한다.
for i in range(n):
    goal = arr[i]
    s,e = 0, n-1
    while s < e:
        if arr[s] + arr[e] == goal:
            if s != i and e != i:
                cnt+=1
                break
            elif s == i:
                s += 1
            elif e == i:
                e-= 1
        elif arr[s] + arr[e] > goal:
            e-=1
        else:
            s+=1
print(cnt)
        