from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
card.sort()

def count_by_range(card,target):
    
    return bisect_right(card, target) - bisect_left(card, target)

for i in check:
    print(count_by_range(card,i),end=' ')

