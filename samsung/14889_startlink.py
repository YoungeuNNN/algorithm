from itertools import combinations
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

possible_team = []
for team in combinations(range(n), n//2):
    possible_team.append(team)

min_stat = 100000
for i in range(len(possible_team)//2):
    team = possible_team[i]
    stat_A =0
    for j in range(n//2): #멤버가 n//2명이므로 n//2만큼 돌린다. 
        member = team[j]
        for k in team:
            stat_A += arr[member][k]
    team = possible_team[-i-1]
    stat_B=0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += arr[member][k]
    min_stat = min(min_stat,abs(stat_A-stat_B))
    
print(min_stat)

    
            
    
        

