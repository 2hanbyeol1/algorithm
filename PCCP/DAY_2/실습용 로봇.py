def solution(command):
    r = 0
    c = 0
    # 상 0 우 1 하 2 좌 3
    d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    for com in command:
        if com == 'R':
            d = (d + 1) % 4
        elif com == 'L':
            d = (d - 1) % 4
        elif com == 'G':
            r = r + dr[d]
            c = c + dc[d]
        elif com == 'B':
            r = r - dr[d]
            c = c - dc[d]
    answer = [r, c]
    return answer