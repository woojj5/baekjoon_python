from itertools import combinations
import sys
arr = list(map(str, sys.stdin.readline().strip()))
ans = set()
st = []
prb = []
for i,j in enumerate(arr):
    if j == '(':
        st.append(i)
    if j == ')':
        prb.append((st.pop(), i))

for i in range(1, len(prb)+1):
    comb = combinations(prb, i)
    for j in comb:
        tmp = arr[:]
        for s,e in j:
            tmp[s] = tmp[e] = ""
        ans.add(''.join(map(str, tmp)))

for i in sorted(list(ans)):
    print(i)