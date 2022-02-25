s = input()
st=[]
stick=0
frag=0

for c in s:
    if c == '(':
        stick +=1
    elif c == ')':
        if st[-1] == '(': 
            stick -= 1
            frag += stick
        else:
            frag +=1
            stick -=1
            
    st.append(c)
print(frag)

            
        


