arr = list(map(str, input().split("-")))

res = []

if len(arr) == 1:
    list_a = list(map(int, ''.join(map(str, arr)).split("+")))
    print(sum(list_a))
else:
    for i in range(len(arr)):
        list_a = list(map(int, arr[i].split("+")))
        if len(list_a) == 1:
            res.append(list_a[0])
        else:
            res.append(sum(list_a))
    result = res[0]
    for i in range(1, len(res)):
        result -= res[i]
    print(result)