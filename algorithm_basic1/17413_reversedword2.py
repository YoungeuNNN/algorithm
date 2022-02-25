import sys
from collections import deque

ls= tuple(sys.stdin.readline().strip())
q=[]
st =[]
result=[]
flag=True

for c in ls:
    if c == '<':
        while st: result.append(st.pop())
        q.append(c)
        flag = False

    elif c == '>':
        q.append(c)
        while q: result.append(q.pop(0))
        flag = True
    
    elif c == ' ':
        if flag and st:
                while st: result.append(st.pop()) #if/for두번 사용하지말고 while로 한번에 처리
                result.append(' ')
        else:
            q.append(c)
            while q: result.append(q.pop(0))
    
    else:
        if flag: # 불리언 변수는 암시적으로 트루 폴스 사용! flag를 이왕이면 트루로 사용할 수 있게 is false 사용은 지양한다.
            st.append(c)
        else:
            q.append(c)

if st:
    while st: result.append(st.pop())

print(''.join(result)) #이렇게 result리스트에 어펜드해서 한번에 조인해서 출력하기 

    



    
    


    


