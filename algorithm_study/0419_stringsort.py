s = list(input())
s.sort()
for c in s:
    if ord(c)>64:
        pos = s.index(c)
        break
    
print(*s[pos:],sep='',end='')
print(sum(map(int,s[:pos])))