import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = []
visited = [[False]*n for _ in range(n)]
three_cnt, two_cnt = 0,0

for _ in range(n):
    arr.append(list(input().rstrip()))
    
move = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x,y):
    visited[x][y] = True
    current_color = arr[x][y]
    for dx,dy in move:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False and arr[nx][ny] == current_color:
            dfs(nx,ny)
                
                
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            three_cnt +=1

print(three_cnt)
                
    
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt +=1
            
print(three_cnt,two_cnt)
