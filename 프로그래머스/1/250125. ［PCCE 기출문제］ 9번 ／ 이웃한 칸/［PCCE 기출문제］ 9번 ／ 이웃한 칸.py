def solution(board, h, w):
    cnt = 0
    for x, y in ((1,0), (-1,0), (0,1), (0,-1)):
        nx = h+x
        ny = w+y
        if 0<= nx < len(board) and 0<= ny < len(board[0]): 
            if board[h][w] == board[nx][ny]:
                cnt+=1
    return cnt