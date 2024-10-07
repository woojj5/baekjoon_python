while True:
    a = input()
    st = []
    if a== '.':
        break
    for i in a:
        if i in '([':
            st.append(i)
        elif i == ']':
            if len(st) != 0 and st[-1]  == '[':
                st.pop()
            else:
                st.append(']')
                break
        elif i == ')':
            if len(st) != 0 and st[-1]  == '(':
                st.pop()
            else:
                st.append(')')
                break
    if len(st) >0:
        print("no")
    else:
        print("yes")