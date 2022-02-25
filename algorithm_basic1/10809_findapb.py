
s = input()

ans = [-1] * (ord('z')-ord('a')+1)

for i,ch in enumerate(s):
    if ans[ord(ch)-ord('a')] == -1:
        ans[ord(ch)-ord('a')] = i

print(*ans)
