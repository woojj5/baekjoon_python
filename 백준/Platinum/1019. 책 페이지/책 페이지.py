num = 1
arr = [0] * 10
n = int(input())
def mak_nine(x):
    while x % 10 != 9:
        for i in str(x):
            arr[int(i)]+=num
        x-=1
    return x

while n > 0:
    n  = mak_nine(n)
    if n < 10:
        for i in range(n+1):
            arr[i] +=num
    else:
        for i in range(10):
            arr[i] += (n //10 + 1) * num
    arr[0] -= num
    num*=10
    n//=10

for i in range(0, 10):
    print(arr[i], end=' ')
