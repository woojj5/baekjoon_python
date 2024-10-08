n = int(input())
max_num = 1
cnt = 1
while max_num < n:
    max_num += (6*cnt)
    cnt+=1
print(cnt)