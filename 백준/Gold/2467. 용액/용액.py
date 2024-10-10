import sys
input = sys.stdin.readline
n = int(input())
liq = list(map(int, input().split()))

left_ind = 0
right_ind  = n-1
ans = abs(liq[left_ind] + liq[right_ind])
l_i = left_ind
r_i = right_ind

while left_ind < right_ind:
    tmp = liq[left_ind] + liq[right_ind]
    if ans > abs(tmp):
        l_i = left_ind
        r_i = right_ind
        ans = abs(tmp)
        if ans == 0:
            break

    if tmp <0:
        left_ind+=1
    else:
        right_ind-=1

print(liq[l_i], liq[r_i])