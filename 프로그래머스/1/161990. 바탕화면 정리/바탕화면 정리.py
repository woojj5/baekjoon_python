def solution(wallpaper):
    answer = []
    nx,ny = 51,51
    mx,my = -1,-1
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            nx = min(nx, i)
            break
    for i in range(len(wallpaper)-1, -1, -1):
        if "#" in wallpaper[i]:
            mx = max(mx, i+ 1)
            break
    row_paper = [list(row) for row in zip(*wallpaper)]
    for i in range(len(row_paper)):
        if "#" in row_paper[i]:
            ny = min(ny, i)
            break
    for i in range(len(row_paper)-1, -1, -1):
        if "#" in row_paper[i]:
            my = max(my, i+ 1)
            break
    answer.append(nx)
    answer.append(ny)
    answer.append(mx)
    answer.append(my)
    return answer