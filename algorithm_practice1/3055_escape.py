import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int,input().split())
arr=[]
water = deque()

for _ in range(r):
    arr.append(list(input().rstrip()))
for i in range(r):
    for j in range(c):
        if arr[i][j]=='.':
            continue
        elif arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == '*':
            water.append((i,j))
    
move = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs():
    q = deque()
    cnt = 0
    q.append((start[0],start[1],cnt))
    arr[start[0]][start[1]] = '.' #고슴도치 칸에는 물이 찰 수 있다.
   
    while q:
        
        temp = len(water)  # 먼저 다음 턴의 물이 찰 곳을 물로 채운다
        for i in range(temp):
            x,y = water.popleft()
            for dx,dy in move:
                nx,ny =x+dx,y+dy
                if 0<=nx<r and 0<=ny<c and arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    if (nx,ny) not in water:
                        water.append((nx, ny))
    
        
        temp = len(q)
        for _ in range(temp):
            x, y, cnt = q.popleft()
        
            for dx,dy in move:
                nx,ny=x+dx,y+dy
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == '.' and (nx,ny,cnt+1) not in q:
                        q.append((nx,ny,cnt+1))
                    elif arr[nx][ny] =='D':
                        return cnt+1    

    return 'KAKTUS'
    
print(bfs())
