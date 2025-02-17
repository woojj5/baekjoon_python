n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if k >= n:
    print(0)  # 모든 센서를 연결할 수 있다면 비용이 0
else:
    arr.sort()
    x = [arr[i+1] - arr[i] for i in range(n-1)]
    x.sort()
    
    for i in range(k-1):
        x.pop()
    
    print(sum(x))
