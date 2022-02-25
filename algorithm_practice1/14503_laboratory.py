import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline
n,m=map(int,input().split())
graph = []
walls = [] #벽 가능 좌표
virus = [] #바이러스 좌표
q = deque()
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            walls.append((i,j))
        if graph[i][j]==2:
            virus.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(start,walls,graph):
    map = deepcopy(graph)
    safe = 0
    for a,b in walls:
        map[a][b] =1
    queue = deque(start)
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m: #만족되면 안되는 조건 
                continue
            if map[nx][ny] ==0:
                map[nx][ny] = 2
                queue.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if map[i][j]==0:
                safe+=1
    return safe
            
            
        
        
            
survive = 0
for i in combinations(walls,3):
    survive = max(survive, bfs(virus,list(i),graph))
print(survive)
    
    
