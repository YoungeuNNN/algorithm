import sys
from collections import deque
#visited배열에 거리를 저장한다.
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(input().strip()))))
q = deque()
visited = []
for _ in range(n):
    visited.append([[0] * (k+1) for i in range(m)])
visited[0][0][k] = 1
visited[0][0] = [1]*(k+1)
q.append((0, 0, k,True))

move = [(-1, 0), (1, 0),(0, 0), (0, -1), (0, 1)]

def bfs():
    while q:
        x, y, crush,morning = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crush]

        for dx, dy in move:
            nx = x+dx
            ny = y+dy

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and crush > 0 and morning:
                    visited[nx][ny][crush-1] = visited[x][y][crush] + 1
                    q.append((nx, ny, crush-1,not morning))
                elif arr[nx][ny] == 0 and visited[nx][ny][crush] == 0:
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                    q.append((nx, ny, crush,not morning))
                elif arr[nx][ny] == 0 and dx==0 and dy==0:
                    visited[nx][ny][crush] +=1 

    return -1


print(bfs())

