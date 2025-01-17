n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l,r = 0, n-1
target= abs(arr[l] + arr[r])
res = [arr[l], arr[r]]
while l<r:
    if abs(arr[l] + arr[r]) < target:
        target = abs(arr[l] + arr[r])
        res = [arr[l], arr[r]]
        if target == 0: break
    if arr[l] + arr[r] < 0:l+=1
    else: r-=1 #처음부터 0인 경우에는 무한루프가 돌아간다. 그래서 같은 경우에 탈출도 만들어야 함.
print(*res)