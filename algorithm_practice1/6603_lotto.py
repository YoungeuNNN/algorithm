import sys
from itertools import combinations
while True:
    input = sys.stdin.readline
    arr = list(map(int, input().split()))
    result = list(combinations(arr[1:],6))
    if arr[0] == 0:
        break

    for i in result:
        for j in i:
            print(j,end=' ')
        print() 
    print()




