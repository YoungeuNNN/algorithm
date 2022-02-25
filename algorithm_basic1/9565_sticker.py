t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    mylist = [list(map(int,input().split())) for i in range(2)]
    
    if n>1:
        mylist[0][1] +=mylist[1][0]
        mylist[1][1]+=mylist[0][0]
        
    for i in range(2,n):
        mylist[0][i] += max(mylist[1][i-1],mylist[1][i-1])
        mylist[1][i] += max(mylist[0][i-1],mylist[0][i-2])
    
    if n>1:
        ans.append(max(mylist[0][n-1],mylist[1][n-1]))
    else:
        ans.append(max(mylist[0][0], mylist[1][0]))

print(*ans,sep='\n')
            


