from collections import deque

n = int(input())
seq=tuple(map(int,input().split()))

st = deque()

comp = 0
ans = [-1] * n #초기값 -1로 세팅하면 추가 연산을 하지 않아도 된다. 

for i in range(n):
    
    while st and (st[-1][0] < seq[i]):
        tmp,idx = st.pop()
        ans[idx] =seq[i]
    st.append([seq[i],i])

print(*ans)


