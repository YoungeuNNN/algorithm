import sys
input = sys.stdin.readline

result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1] #상하좌우 이동방식

def dfs(x,y,cnt,sum):
    global result,max_val #맥스 값 비교 위해    
    if sum + max_val*(4-cnt) <result:
        return
    if cnt >= 4: 
        if result<sum:
            result = sum
        return
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if cnt ==2:
                visited[nx][ny] = True
                dfs(x,y,cnt+1,sum+arr[nx][ny])
                visited[nx][ny] = False
            
            visited[nx][ny] = True
            dfs(nx,ny,cnt+1,sum+arr[nx][ny])
            visited[nx][ny] = False #다른 테트로미노에서 사용 할 수 있도록 


n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
arr = [list(map(int,input().split())) for _ in range(n)]

max_val = max(max(*arr))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,arr[i][j])
        visited[i][j]= False

print(result)
