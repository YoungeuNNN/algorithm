
import sys
from collections import deque
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    
    visited[n] = True
    queue = deque([n]) #n은 시작원소
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


input = sys.stdin.readline
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

#make adjacency list
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#sort ->무작위 순서로 된걸 솔트해줌
for i in range(1,n+1):
    graph[i].sort()

print(graph)
dfs(v)
visited = [False]*(n+1)
print()
bfs(v)
