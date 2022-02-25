n,m = map(int,input().split())
tree = list(map(int,input().split()))

l,r = 0,max(tree)

while r>=l:
    mid = (l+r)//2
    cnt = sum([n-mid for n in tree if n-mid>0])
    if cnt>=m:
        l = mid+1
    else:
        r = mid-1

print(r)