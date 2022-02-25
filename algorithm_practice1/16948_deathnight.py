import sys
from collections import deque

input = sys.stdin.readline
n=int(input())
r1,c1,r2,c2=map(int,input().split())
dist =[[-1]*n for _ in range(n)] #이동 횟수 저장 배열 
q = deque()
q.append((r1,c1))

dist[r1][c1] = 0
move = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]

while q:
    x,y =q.popleft()
    for dx,dy in move:
        
        nx = x+dx
        ny = y+dy
  
        if 0<=nx<n and 0<=ny<n and (dist[nx][ny]==-1 or dist[nx][ny]>dist[x][y]+1):
            dist[nx][ny] = dist[x][y]+1
            q.append((nx,ny))
            
        
        
print(dist[r2][c2])
    
    

