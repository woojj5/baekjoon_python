def solution(arr):
    ind = len(arr)//2 + 1
    inf = float("inf")
    max_ind = [[-inf for i in range(ind)]for i in range(ind)]
    min_ind = [[inf for i in range(ind)]for i in range(ind)]
    for i in range(ind):
        max_ind[i][i] = int(arr[2*i])
        min_ind[i][i] = int(arr[2*i])
    for c in range(ind):
        for i in range(ind - c):
            j = i+c
            for k in range(i,j):
                if arr[2*k+1] == "+":
                    max_ind[i][j] = max(max_ind[i][j], max_ind[i][k] + max_ind[k+1][j])
                    min_ind[i][j] = min(min_ind[i][j], min_ind[i][k] + min_ind[k+1][j])
                elif arr[2*k+1] == "-":
                    max_ind[i][j] = max(max_ind[i][j], max_ind[i][k] - min_ind[k+1][j])
                    min_ind[i][j] = min(min_ind[i][j], min_ind[i][k] - max_ind[k+1][j])
    answer = max_ind[0][-1]
    return answer