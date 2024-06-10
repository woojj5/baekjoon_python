n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = arr[0]
for i in range(1, n):
	s += arr[i]
	for j in range(0, i):
		s += arr[j]
print(s)