def solution(board):
    def won(arr, id):
        for row in arr:
            if row == [id, id, id]:
                return 1
        for col in range(3):
            if [arr[row][col] for row in range(3)] == [id, id, id]:
                return 1
        if [arr[0][0], arr[1][1], arr[2][2]] == [id, id, id]:
            return 1
        if [arr[0][2], arr[1][1], arr[2][0]] == [id, id, id]:
            return 1
        return 0
    
    answer = -1
    arr = [list(row) for row in board]
    o_count,x_count = 0,0
    for i in arr:
        for j in i:
            if j == "O":
                o_count+=1
            if j == "X":
                x_count+=1
    if not (o_count == x_count or o_count == x_count + 1):
        return 0

    # O 혹은 X만 승리조건을 만족해야 함.
    if won(arr, 'O') and won(arr, 'X'):
        return 0
    
    # O가 승리했다면 o_count == x_count + 1이어야 함.
    if won(arr, 'O') and o_count != x_count + 1:
        return 0
    
    # X가 승리했다면 o_count == x_count 여야 함.
    if won(arr, 'X') and o_count != x_count:
        return 0

    return 1