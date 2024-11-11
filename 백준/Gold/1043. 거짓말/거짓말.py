n,m = map(int, input().split())
tru = set(input().split()[1:])
party = []
for i in range(m):
    party.append(set(input().split()[1:]))

for i in range(m):
    for p in party:
        if p & tru:
            tru = tru.union(p)
cnt = 0
for p in party:
    if p & tru:
        continue
    cnt+=1
print(cnt)