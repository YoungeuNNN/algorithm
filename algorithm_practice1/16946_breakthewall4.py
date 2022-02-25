import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,list(input().rstrip()))) for _ in range(n)]
#플러드필 알고리즘을 사용해보자!
#https://ku-hug.tistory.com/153 참고
#모든 좌표의 인접 0의 갯수가 필요하다,값을 하나만 뽑아내는게 아니라는것

move = [(-1,0),(1,0),(0,-1),(0,1)]
visited = [[False]*m for _ in range(n)]
zeros = [[0]*m for _ in range(n)]
group = 1
info = {} #각 그룹의 좌표를 저장할 딕셔너리 
info[0] = 0 #1번부터 저장되니까 0번 에러 안나게 초기화


def bfs(i,j): #인접한 0들을 묶어줌
    q = deque()
    q.append((i,j))
    cnt = 1
    while q:
        x,y = q.popleft()
        zeros[x][y] = group
        for dx,dy in move:
            nx,ny=x+dx,y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[nx][ny] or arr[nx][ny]==1:
                continue
            visited[nx][ny]=True
            q.append((nx,ny))
        
            cnt+=1 #bfs시 넓게 검색하는것이므로 cnt올리기만 하면됨
    return cnt                
            
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]: #0이고 아직 방문 안했으면
            visited[i][j] =True 
            info[group] = bfs(i,j) #각 그룹별 0의 갯수
            group +=1
            
for i in range(n):
    for j in range(m):
        addList = set()
        if arr[i][j]: #벽이라면 
            for dx,dy in move:
                nx,ny =i+dx,j+dy
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                addList.add(zeros[nx][ny])
            for add in addList:
                arr[i][j] += info[add]
                arr[i][j] %=10
for g in arr:
    print(''.join(map(str,g)))


    
    
