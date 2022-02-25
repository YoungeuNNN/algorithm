n = int(input())
n = 1000 - n
cnt = 0
lst = [500,100,50,10,5,1]
for i in lst:#최소 단위가 있을 때 쓰는 방법
    cnt += n//i
    n%=i

if n != 0:
    cnt = -1 #거스름을 줄 수 없을 때 -1을 출력한다. 
print(cnt)