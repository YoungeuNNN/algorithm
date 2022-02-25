
n = int(input())
ls = []
for i in range(n):
    c = 0
    s = input()
    for j in s:
        if j == '(':
            c += 1
        elif j == ')':
            c -= 1
        if c < 0:
            ls.append('NO')
            break

    if c == 0: 
        ls.append('YES')
    elif c > 0:
        ls.append('NO')
for k in ls:
    print(k)