init = int(input())
cnt = 0
res = -1000
while res != init:
    if cnt == 0:
        cnt = cnt + 1
        res = 10 * (init%10) + (init//10 + init%10)%10
        #print(res)
    else:
        res = 10 * (res%10) + (res//10 + res%10)%10
        cnt = cnt + 1
        #print(res)
        #break
    
print(cnt)
    
