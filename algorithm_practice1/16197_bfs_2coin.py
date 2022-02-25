import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

board = []
temp = []
coin = deque()

for i in range(n):
    board.append(list(input().strip())) #리스트가 알아서 잘려서 들어간다
    for j in range(m):
        if board[i][j] == 'o':
            temp.append((i,j)) #coin인덱스를 찾아서 넣어줌 


move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(): #dfs는 보통 재귀로 돌아가지만 bfs는 그렇지 않음
    while coin:
        x1,y1,x2,y2,cnt=coin.popleft()
        if cnt>=10:
            return -1
        for dx, dy in move:
            nx1 = x1+dx
            ny1 = y1+dy
            nx2 = x2+dx
            ny2 = y2+dy

            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:#값이 범위 안에 속하는지 체크
                #벽이라면
                if board[nx1][ny1] == "#":
                    nx1,ny1 = x1,y1 #더하기 전의 자리로 돌아간다.
                if board[nx2][ny2] == "#":
                    nx2,ny2 = x2,y2
                coin.append((nx1,ny1,nx2,ny2,cnt+1))
            elif 0<=nx1<n and 0<=ny1<m: #coin2떨어짐
                return cnt+1
            elif 0<=nx2<n and 0<=ny2<m: #coin1이 떨어짐
                return cnt+1
            else:
                continue
    return -1


coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
print(bfs())




