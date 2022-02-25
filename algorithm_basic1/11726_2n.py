t = int(input())   
ans = []
s = [0, 1, 2, 4]
for i in range(t):
    ans.append(int(input())) 

for i in range(4,12):
    s.append(s[i-3]+s[i-2]+s[i-1])

for i in ans:
    print(s[i])
