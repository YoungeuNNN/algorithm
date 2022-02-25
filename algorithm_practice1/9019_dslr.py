import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
q = deque()
result = []

for _ in range(t):
    f, dest = map(int, input().split())
    q.append((f, ''))
    visited = [False]*10000
    while q:
        a, ans = q.popleft()
        if a == dest:
            result.append(ans)
            break

        d = 2*a % 10000
        if not visited[d]:
            visited[d] = True
            q.append((2*a % 10000, ans+'D'))

        s = 9999 if a == 0 else a-1
        if not visited[s]:
            visited[s] = True
            q.append((s, ans+'S'))

        l = (a % 1000)*10 + (a//1000)
        if not visited[l]:
            q.append((l, ans+'L'))
        r = (a % 10)*1000 + (a//10)
        if not visited[r]:
            q.append((r, ans+'R'))
    q.clear()

    


print(*result,sep='\n')
