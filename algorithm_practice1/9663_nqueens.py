n=int(input())
col=[0 for _ in range(n)]
result = 0

def adjacent(x):
    for i in range(x):
        if col[x]==col[i] or abs(col[x]-col[i])==x-i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result +=1
    else:
        for i in range(n):
            col[x]=i
            if adjacent(x):
                dfs(x+1)
                

dfs(0)
print(result)
            