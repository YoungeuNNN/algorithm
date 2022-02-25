import sys

input = sys.stdin.readline
n = int(input())
net = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(int(input())):
    a,b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)

def dfs(node):
    visited[node] = 1
    for i in net[node]:
        if visited[i] ==0:
            visited[i] = 1
            dfs(i)

dfs(1)
print(''.join(list(map(str,visited))).count('1')-1)


    

    
