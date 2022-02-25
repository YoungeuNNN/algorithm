from math import factorial
t =int(input())

for _ in range(t):
    a,b = map(int,input().split())
    print(factorial(b) // (factorial(a)*factorial(b-a)))
    