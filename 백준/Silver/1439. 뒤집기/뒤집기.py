a = [i for i in input()]
z_cnt = 0
o_cnt = 0
if a[0] == '0':
    z_cnt+=1
else:
    o_cnt+=1
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        if a[i+1] == '0':
            z_cnt+=1
        else:
            o_cnt+=1
#print(a)
print(min(o_cnt, z_cnt))


