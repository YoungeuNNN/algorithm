import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(n):
    for i in arr[n]:
        if visited[i] == False:
            visited[i] =True
            dfs(i)
    
count = 0
for i in range(1,n+1):
    if visited[i] == False: #그래프가 끊겨도 다시 볼 수 있음
        count+=1 
        dfs(i)
print(count)



