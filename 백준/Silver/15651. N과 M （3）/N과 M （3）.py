n,l = map(int, input().split())
s = []

def back():
    if len(s) == l:
        print(" ".join(map(str, s)))
        return 
    
    for i in range(1, n+1):
        s.append(i)
        back()
        s.pop()
back()