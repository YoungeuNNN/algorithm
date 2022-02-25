import sys
input = sys.stdin.readline

n=int(input())
w = list(map(int,input().split()))
result = [0 for _ in range(n)]
maxV=0

def bfs(sum):
    global maxV
    if len(w)==2:
        if sum>maxV:
            maxV = sum
        return
    else:
        for i in range(1,len(w)-1):
            r = w[i-1]*w[i+1]
            temp = w[i]
            del w[i]
            bfs(sum+r)
            w.insert(i,temp)
    
bfs(0)      
print(maxV)