from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]


move = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque()
q.append((0,0,board[0][0]))
maxLen = 0
while q:
    x,y,ch= q.popleft()
    maxLen = max(maxLen,len(ch))
    for dx,dy in move:
        nx,ny = x+dx, y+dy
        
        if 0<=nx<n and 0<=ny<m and (board[nx][ny] not in ch):
            q.append((nx,ny,ch+board[nx][ny]))
        
        
print(maxLen)
