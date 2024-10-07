import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    x,r = map(int, input().split())
    arr.append((x-r, i))
    arr.append((x+r, i))
arr.sort()
st = []
for i in range(2*n):
    x,r = arr[i]
    if len(st) == 0:
        st.append(arr[i])
    elif st:
        if st[-1][1] == r:
            st.pop()
        else:
            st.append(arr[i])

if len(st) == 0:
    print("YES")
else:
    print("NO")