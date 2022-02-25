e,s,m = map(int,input().split())
et,st,mt = 0,0,0
year = 0
while 1:
    et+= 1
    st+=1
    mt+=1
    year+=1
    if et>15:
        et=1
    if st>28:
        st=1
    if mt>19:
        mt=1
    
    if et==e and st==s and mt==m:
        break

print(year)
