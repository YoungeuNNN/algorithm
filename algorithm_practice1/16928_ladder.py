from collections import deque
n,m= map(int,input().split())
k=101
g=[*range(k)]#기억해두기 
for _ in range(n+m):
    x, y = map(int, input().split())
    g[x] = y


dist=[-1]*k
dist[1]=0 #필요한 변수는 초기화 하는 것 잊지 않기,1에서 시작함
#간선리스트g, 주사위를 몇번굴러야 index에 해당하는 숫자에 도착할 수 있는지카운팅하는 리스트
queue = deque() #1에서 시작하므로 append 1 하기
queue.append(1)

#bfs할때는 q에서 팝해서 쓴다.
while queue:
    x= queue.popleft()
    for i in range(1,7):
        y = x+i
        if y>100:
            break
        y=g[y]
        if dist[y]==-1 or dist[y]>dist[x]+1:
            dist[y] = dist[x]+1
            queue.append(y)
            
print(dist[100])
            
        
    
