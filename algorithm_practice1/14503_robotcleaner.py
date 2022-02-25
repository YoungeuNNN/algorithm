from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())
zone = []
cleaned = [[False]*m for _ in range(n)]
cleaned[r][c] = True

for _ in range(n):
    zone.append(list(map(int,input().split())))

move = [(-1,0),(0,1),(-1,0),(0,-1)]

def dfs(x,y,d):
    if zone[x][y] == 0:
        zone[x][y] == 2
    for _ in range(4):
        nd = (d+3)%4
        dx,dy = move[nd][0], move[nd][1]
        nx,ny = x+dx,x+dy
        if 0<=nx<n and 0<=ny<m and zone[nx][ny] ==0:
            dfs(nx,ny,nd)
            print(nx,ny,nd)
            return
        d = nd
    nd = (d+2) %4
    nx = x+move[nd][0]
    ny = y+move[nd][1]
    if zone[nx][ny] == 1:
        return
    dfs(nx,ny,d)
    
    

dfs(r,c,d)
print(sum(i.count(2) for i in zone))


q = deque()


