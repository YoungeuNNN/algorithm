import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
parents= [0 for _ in range(n+1)]
tree= [[] for _ in range(n+1)]

for _ in range(n-1):#노드가 7개면 연결은 6개
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i,tree,parents)
        
dfs(1,tree,parents)
for i in range(2,n+1):
    print(parents[i])