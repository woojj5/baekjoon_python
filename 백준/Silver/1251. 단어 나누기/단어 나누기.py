st = input()
res = []
for i in range(1, len(st) - 1):
    for j in range(i+1, len(st)):
        str1= st[:i][::-1]
        str2= st[i:j][::-1]
        str3= st[j:][::-1]
        res.append(str1+str2+str3)
print(min(res))