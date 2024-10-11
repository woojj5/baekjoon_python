n,k,p, x = map(int, input().split())
num2digital = {
    '0': [1, 1, 1, 1, 1, 1, 0],
    '1': [0, 1, 1, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1],
    '3': [1, 1, 1, 1, 0, 0, 1],
    '4': [0, 1, 1, 0, 0, 1, 1],
    '5': [1, 0, 1, 1, 0, 1, 1],
    '6': [1, 0, 1, 1, 1, 1, 1],
    '7': [1, 1, 1, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1]
}

X = str(x).zfill(k)
x_transform = [num2digital[x] for x in X]
possible = 0

for i in range(1, n+1):
    elev = str(i).zfill(k)
    ele_transform = [num2digital[e] for e in elev]

    diff_cnt = 0

    for x,e in zip(x_transform, ele_transform):
        for i,j in zip(x, e):
            if i!= j:
                diff_cnt+=1
            if diff_cnt > p:
                break
    if diff_cnt <= p and diff_cnt:
        possible+=1
print(possible)