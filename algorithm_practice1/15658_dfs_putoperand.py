import sys
input = sys.stdin.readline
n=int(input())
nums = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
max, min = -10**8, 10**8

def dfs(i,res,add,sub,mul,div):
    global max,min
    if i==n: #i로 재귀의 깊이 알 수 있다
        if res>max:
            max=res
        if res<min:
            min = res
        return
    else:
        if add:
            dfs(i+1,res+nums[i],add-1,sub,mul,div)
        if sub:
            dfs(i+1,res-nums[i],add,sub-1,mul,div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1,int(res/nums[i]), add, sub, mul, div-1)

dfs(1,nums[0],add,sub,mul,div)
print(max,min,sep='\n')