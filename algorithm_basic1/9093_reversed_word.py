n = int(input())
for i in range(n):
    s = input()
    for j in s.split():
        print(j[::-1],end=' ')
    print()