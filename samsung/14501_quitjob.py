n = int(input())
t=[]
p=[]
dp = []
for _ in range(n):
   a,b= map(int,input().split())
   t.append(a)
   p.append(b)
   dp.append(p)
dp.append(0) #마지막날 0을 더해줌 왜? 인덱스 레인지 때문인지


