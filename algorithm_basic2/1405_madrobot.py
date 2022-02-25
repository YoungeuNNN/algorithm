n,*d= map(int,input().split())
d = [*map(lambda x: x*0.01,d)]
visited = [[False] * 29 for _ in range(29)]
answer =0
dx,dy = [1,-1,0,0],[0,0,-1,1]

def dfs(x,y,depth,per_stack):
    global answer
    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y +dy[i]
        if not visited[nx][ny]:
            if depth >= n:
                answer += per_stack *d[i]
            else:
                dfs(nx,ny,depth+1,per_stack * d[i])
    
    visited[x][y] = False

dfs(14,14,1,1)
print(answer)