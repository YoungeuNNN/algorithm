n,r = map(int,input().split())
arr = [[] for i in range(n)]
visited = [False]*n

for _ in range(r):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

print(arr)
def dfs(n,count):

    if count ==4:
        print(1)
        exit()
    for i in arr[n]:
        if not visited[i]: #dfs 이고 연결성을 확인하는 것이므로 true 했다가 false해야함
            visited[i] = True
            dfs(i,count+1)
            visited[i] = False


for i in range(n): #다시할때마다 false로 초기화 필요
    visited[i] =True
    dfs(i,0) #count 필요할 때 dfs밖에서 해야 함! dfs는 재귀 함수이기 때문에 반복적인 방법만 함
    visited[i] = False

print(0)


    
