from collections import Counter
from collections import deque
n = int(input())
seq = list(map(int, input().split()))
count = Counter(seq)

st = deque()
ans = [-1] * n  # 초기값 -1로 세팅하면 추가 연산을 하지 않아도 된다.

for i in range(n):
    while st and (count.get(st[-1][0]) < count.get(seq[i])):
        tmp, idx = st.pop()
        ans[idx] = seq[i]
    st.append([seq[i], i])

print(*ans)
