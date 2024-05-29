a = int(input())
for i in range(a):
    n,m = map(int, input().split())
    if m == n:
        print(1)
    else:
        res_m, res_b, res_c = m, n, m-n
        temp_m = temp_b = temp_c = 1
        for i in range(1, res_m+1):
            temp_m = i * temp_m
        for i in range(1, res_b+1):
            temp_b = i * temp_b
        for i in range(1, res_c+1):
            temp_c = i * temp_c

        res = temp_m //(temp_b * temp_c)
        print(res)