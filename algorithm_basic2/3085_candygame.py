n = int(input())
lst = [[0]*n for _ in range(n)] #가변 이차원 리스트 
length = 0
breadth = 0
maxlen = 0
for i in range(n):
    temp = input()
    for j,value in enumerate(temp):
        lst[i][j] = value

lst2 = lst[:]
maxlist = [[0]*n for _ in range(n)] #크기가 고정된 이차원리스트 


for i in range(n):
    for j in range(n-1):
        lst[i][j],lst[i][j+1] = lst[i][j+1],lst[i][j]
        for k in range(0,n):
            if lst[i][j] == lst[i][k]:
                length +=1
            elif lst[i][j] != lst[i][k]:
                length = 0
            
            if lst[i][j] == lst[k][j]:
                breadth +=1
            elif lst[i][j] != lst[k][j]:
                breadth = 0
        maxlist[i][j] = max(length,breadth)
        lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
        length = 0
        breadth = 0

for i in range(n-1):
    for j in range(n):
        lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
        for k in range(0, n):
            if lst[i][j] == lst[i][k]:
                length += 1
            elif lst[i][j] != lst[i][k]:
                length = 0

            if lst[i][j] == lst[k][j]:
                breadth += 1
            elif lst[i][j] != lst[k][j]:
                breadth = 0
    
        maxlist[i][j] = max(length, breadth,maxlist[i][j])
        lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
        length = 0
        breadth = 0
        


n=0
for list in maxlist:
    if n<max(list):
        n = max(list)
print(n)
            


        
