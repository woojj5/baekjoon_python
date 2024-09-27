n = int(input())
lista = list(map(int, input().split()))
dic = dict()
res = [-1] * len(lista)
stack  = []
for i in lista:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] +=1

for i in range(n):
    while stack and dic[lista[stack[-1]]] < dic[lista[i]]:

        res[stack.pop()] = lista[i]
    stack.append(i)
for i in res:
    print(i, end = " ")