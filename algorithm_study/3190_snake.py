from collections import deque
n = int(input()) #보드의 크기
k = int(input()) #사과의 갯수
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 2 #사과의 위치 초기화
l = int(input())
cmd = dict() #회전 명령어 입력
for _ in range(l):
    a,b = input().split()
    cmd[int(a)] = b
print(cmd)
move = [(0,1),(1,0),(0,-1),(-1,0)]

x,y = 0,0
arr[x][y] =1
direction = 0

def turn(key):
    global direction
    if key=='L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
        
q = deque()
q.append((0,0))
cnt = 0
while True:
    cnt +=1
    x += move[direction][0]
    y += move[direction][1]
    
    if x<0 or x>=n or y<0 or y>=n:
        break
    if arr[x][y] ==2:
        arr[x][y] =1
        q.append((x,y))
        if cnt in cmd:
            turn(cmd[cnt])
        
    elif arr[x][y] ==0:
        arr[x][y] = 1
        q.append((x,y))
        nx,ny = q.popleft()
        arr[nx][ny] = 0
        if cnt in cmd:
            turn(cmd[cnt])
    else:
        break
    
print(cnt)
