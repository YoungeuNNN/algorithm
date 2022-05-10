from collections import deque

n,l,r = map(int,input().split())
nation = [list(map(int,input().split())) for _ in range(n)]

move = [(-1,0),(1,0),(0,-1),(0,1)]

is_move = False
def bfs(a,b):
    q = deque()
    temp = []
    q.append((a,b))
    temp.append((a,b)) #q에도, temp에도 담는다. 왜? temp에는 국경선을 공ㅇ하는 나라들의 좌표값
    while q:
        x,y = q.popleft()
        for dx,dy in move:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] ==0: