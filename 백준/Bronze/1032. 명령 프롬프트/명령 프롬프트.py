n = int(input())
tmp = ""
res = ""
for i in range(n):
    a = input()
    if n == 1:
        print(a)
        break
    elif tmp == "":
        tmp = a
        #print(tmp)
        continue
    else:
        for j in range(len(tmp)):
            if tmp[j] != a[j]:
                res = res + "?"
            else:
                res = res + a[j]
            if j == len(tmp) - 1 and i != n-1:
                tmp = res
                res = ""
        if i == n-1:
            print(res)
            break
    