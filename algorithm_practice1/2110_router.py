n,c = map(int,input().split())
h = [int(input()) for _ in range(n)]
h.sort()

l = 1 #최소거리
r = h[-1] - h[0]#최대거리
while l<=r:
    mid = (l+r)//2
    cur = h[0]
    cnt = 1 #첫번째 집에는 무조건 설치한다.
    for i in range(2, len(h)):
        if h[i] >= cur+mid:
            cnt +=1 
            cur = h[i]
     
    if cnt >=c:
        l = mid+1
    else:
        r = mid-1
        
print(r)
    