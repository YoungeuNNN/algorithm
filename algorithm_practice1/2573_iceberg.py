import sys
import collections
input = sys.stdin.readline
n,m = map(int,input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int,input().split())))

move = [(-1,0),(1,0),(0,-1),(0,1)]
q = collections.deque()
day =0
check = False

def bfs(a,b):
    q.append((a,b))
    while q:
        x,y = q.popleft()
        visited[x][y] = True
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<= ny<m:
                if ice[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif ice[nx][ny] == 0:
                    count[x][y] +=1
    return 1


while  True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if ice[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
            
       # 빙산을 깍아줌
    for i in range(n):
        for j in range(m):
            ice[i][j] -= count[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
    if not result:
        break
    if len(result)>=2:
        check = True
        break
    day +=1
    
if check:
    print(day)
else:
    print(0)
