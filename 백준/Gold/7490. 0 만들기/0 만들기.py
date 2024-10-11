import sys
input = sys.stdin.readline
def recur(n, idx, cur):
    if idx == N:
        ans = eval(cur.replace(" ", ""))
        if ans == 0:
            ans_list.append(cur)
        return 
    else:
        n_id = idx +1
        
        recur(n, n_id, cur + ' ' + str(n_id))
        
        recur(n, n_id, cur + '+' + str(n_id))
        
        recur(n, n_id, cur + '-' + str(n_id))

T = int(input())  # First input for the number of test cases
for i in range(T):  # First input for the number of test cases
    ans_list = []
    N = int(input())  # Input for the current value of N
    recur(N, 1, '1')
    ans_list.sort()
    for a in ans_list:
        print(a)
    print()