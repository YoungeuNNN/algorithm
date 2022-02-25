s = input()
e = input()
while e:
    if s == e:
        print(1)
        break
    elif len(s) == len(e) and s != e:
        print(0)
        break
    elif s != e:
        if e[-1] == 'A':
            e = e[:-1]
        elif e[-1] == 'B':
            e = e[:-1]
            e = e[::-1]

        
         
        