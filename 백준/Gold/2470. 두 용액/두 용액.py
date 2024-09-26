n  = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = n-1
ans = abs(arr[left] + arr[right])
fin = [arr[left], arr[right]]
while left < right:
    left_val = arr[left]
    right_val = arr[right]
    sum = left_val + right_val
    if abs(sum) < ans:
        ans = abs(sum)
        fin = [left_val, right_val]
        if ans == 0:
            break
    if sum < 0:
        left+=1
    else:
        right-=1
    
print(fin[0], fin[1])
