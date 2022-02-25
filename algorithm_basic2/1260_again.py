from collections import deque
import sys

def dfs(n): #재귀함수가 스택 역할 함 
    print(n,end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n): #그냥 하나씩 꺼내서 큐에 넣으면됨
    visited[n]= True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True








input = sys.stdin.readline
n,m,v= map(int,input().split())
graph =[[] for _ in range(n+1)] #2중 포문 선언
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

dfs(v)
print()
visited = [False]*(n+1)

bfs(v)



