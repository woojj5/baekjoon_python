n = int(input())
arr = list(map(int, input().split())) # 연산될 숫자 배열
opr = list(map(int, input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈

maxnum =-int(1e9)
minnum = int(1e9)

def operator_insertion(add, sub, multi, divi, total, idx):
	global maxnum, minnum
	if idx == n:
		maxnum = max(maxnum, total)
		minnum = min(minnum, total)
		return 
	if add:
		operator_insertion(add-1, sub, multi, divi, total+ arr[idx], idx+1) 
	if sub:
		operator_insertion(add, sub-1, multi, divi, total- arr[idx], idx+1) 

	if multi:
		operator_insertion(add, sub, multi-1, divi, total* arr[idx], idx+1) 

	if divi:
		operator_insertion(add, sub, multi, divi-1, int(total/arr[idx]), idx+1) 


operator_insertion(opr[0], opr[1], opr[2], opr[3], arr[0], 1)
print(maxnum)
print(minnum)