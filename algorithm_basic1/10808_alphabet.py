from collections import Counter

str =input()

count = Counter(str)
ans = [0]*(ord('z')-ord('a')+1)
for key,val in count.items():
    ans[ord(key)-ord('z')-1] = val

print(*ans)

