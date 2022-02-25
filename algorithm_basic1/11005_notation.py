from sys import stdin

n,b = stdin.readline().split()
b = int(b)
ans = 0
#와 잘짰다 나
remainder = [str(i) for i in range(0,10)] + [chr(i) for i in range(ord('A'),ord('Z')+1)]


for i,num in enumerate(n[::-1]):
    ans += remainder.index(num) * b**i

print(ans)

    

