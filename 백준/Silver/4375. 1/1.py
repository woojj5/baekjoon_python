while True:
    num = ""
    cnt = 0
    try:
        n = int(input())
    except:
        break
    while True:
        cnt+=1
        num = num + "1"
        if int(num) % n == 0:
            print(cnt)
            break