def solution(video_len, pos, op_start, op_end, commands):
    def skip(t):
        if op_start <= t <= op_end:
            return op_end
        return t
    def str2sec(s):
        mm,ss = map(int, s.split(":"))
        return 60*mm + ss
    def sec2str(t):
        mm,ss = divmod(t, 60)
        return f'{mm:02d}:{ss:02d}'
    video_len, pos, op_start, op_end = map(str2sec, [video_len, pos, op_start, op_end])
    pos = skip(pos)
    for c in commands:
        if c == 'next':
            pos = min(video_len, pos+10)
        else:
            pos = max(0, pos-10)
        pos = skip(pos)
    pos = sec2str(pos)
    return pos