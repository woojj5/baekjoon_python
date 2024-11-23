import copy
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
res = copy.deepcopy(arr)
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    # 점화식 초기값 설정
    res[1] = arr[0] + arr[1]
    res[2] = max(arr[0], arr[1]) + arr[2]

    # 일반 점화식
    for i in range(3, n):
        res[i] = max(res[i - 3] + arr[i - 1], res[i - 2]) + arr[i]

    # 결과 출력
    print(res[n - 1])