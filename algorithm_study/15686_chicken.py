import sys
from itertools import combinations
from syslog import LOG_DEBUG
input = sys.stdin.readline
n,m = map(int,input().split())
town,chicken,home = [],[],[]
result = 10e9 #모든 치킨거리의 합 중 가장 작은거

for i in range(n):
    temp = list(map(int, input().split()))
    for j,elem in enumerate(temp): 
        if elem == 2:
            chicken.append((i,j))
        elif elem ==1:
            home.append((i,j))
            
for comb in combinations(chicken,m):
    temp = 0
    for elem in home:
        chicken_len = 10e9
        for j in range(m):
            chicken_len = min(chicken_len,abs(elem[0]-comb[j][0])+abs(elem[1]-comb[j][1]))

        # print(type(elem),elem) #tuple
        # print(type(elem[0]),elem[0]) #int
        # print(type(comb),comb) #tuple list
        # print(type(comb[0]),comb[0]) #tuple
        # print(type(comb[0][0]), comb[0][0]) #int
        # print(chicken_len)
        temp += chicken_len
    result = min(result,temp)
print(result)



      
