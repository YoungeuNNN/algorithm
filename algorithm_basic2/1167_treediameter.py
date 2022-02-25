import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n = int(input())
tree = [[] for n in range(n+1)]
result = [0 for _ in range(n+1)]
result2 = [0 for _ in range(n+1)]
for i in range(1,n+1):
    l = list(map(int,input().lstrip(str(i)).split()))
    l.reverse()
    while l:
        temp = l.pop()
        if temp==-1:
            break
        temp2 = l.pop()
        tree[i].append((temp,temp2))
def dfs(root,matrix,result):
    for v,w in matrix[root]:
        if result[v] == 0:
            result[v] += result[root] + w #아직 방문한 적 없으면 여기까지 온 비용에 현재 w를 더한다.
            dfs(v,matrix,result)    

dfs(1,tree,result)
result[1]=0
maxresult = 0
for i in range(len(result)):
    if result[i]>maxresult:
        maxresult = result[i]
        index = i

dfs(index, tree, result2)
result2[index]=0
print(max(result2))