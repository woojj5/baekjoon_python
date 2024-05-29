n = int(input())
line = 1
while line < n:
    n = n- line
    line = line + 1

if line % 2 == 0:
    a =  n
    b =  line - n +1

elif line % 2 == 1:
    a =  line - n +1
    b =  n

print("%d/%d" %(a,b))
