
import sys
input=sys.stdin.readline
arr=[list(map(int,input().split())) for _ in range(9)]
blank=[]
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            blank.append((i,j))
  
def checkRow(x,a):
    for i in range(9):
        if a == arr[x][i]:
            return False
    return True 
def checkCol(y,a):
    for i in range(9):
        if a == arr[i][y]:
            return False
    return True

def checkRect(x,y,a):
    x = x//3*3
    y = y//3*3
    for i in range(3):
        for j in range(3):
            if a == arr[x+i][y+j]:
                return False
    return True
    
           
def dfs(n): #0의 갯수, 블랭크에들어있는 원소의 갯수
    if n==len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)
    
    for i in range(1,10): #blank에 1부터 10까지 모두 넣어본다.
        x=blank[n][0]
        y=blank[n][1]
        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            arr[x][y] = i
            dfs(n+1)
            #arr[x][y]=0 #다시 0으로 만들어줘야 다른 경우의 수 찾을 수 있음 근데 굳이? 
            
        

dfs(0)
        