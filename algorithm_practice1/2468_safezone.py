import sys
input = sys.stdin.readline
n = int(input())
arr = []
sys.setrecursionlimit(300000)
for _ in range(n):
    arr.append(list(map(int,input().split())))


move = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(x,y,h):
    for dx,dy in move:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny]>h:
            visited[nx][ny]= True
            dfs(nx,ny,h)

ans=1
for k in range(max(map(max,arr))):#가장 큰 값을 찾아 그 수 만큼 반복
    visited = [[False]*n for _ in range(n)] #매번 visited 배열을 새로 사용해야 하므로
    safe = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                safe +=1 
                visited[i][j] = True
                dfs(i,j,k)
    ans = max(ans,safe)
    
print(ans)
