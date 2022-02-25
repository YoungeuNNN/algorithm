from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,list(input().rstrip()))))

move = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque()

def bfs(x,y,arr):
    cnt = 1
    arr[x][y] = 0
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
        
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx,ny))
                cnt +=1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] ==1:
            result.append(bfs(i,j,arr))

result.sort()
print(len(result))
print(*result,sep='\n')
    
  

