from collections import defaultdict

def find_word(k, w):
    minval, maxval = len(w)  + 1, -1
    alpha = defaultdict(list)
    for i in range(len(w)):
        alpha[w[i]].append(i)

    for idx in (alpha.values()):
        if len(idx) < k:
            continue
        for i in range(len(idx) - k + 1):
            minval = min(minval, idx[i+k-1] - idx[i] + 1)
            maxval = max(maxval, idx[i+k-1] - idx[i] + 1)
    return minval, maxval

for i in range(int(input())):
    w = input().strip()
    k = int(input())
    minval, maxval = find_word(k, w)
    if maxval == -1:
        print(maxval)
    else:
        print(minval, maxval)
