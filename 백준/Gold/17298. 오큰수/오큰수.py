n = int(input())
lista = list(map(int, input().split()))
res = [-1] * n
stack = [0]
for i in range(1, n):
    while stack and lista[stack[-1]] < lista[i]:
        res[stack.pop()]  =  lista[i]
    stack.append(i)
for i in res:
    print(i, end = " ")