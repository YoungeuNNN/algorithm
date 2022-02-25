n= int(input())
w=[]
for _ in range(n):
    w.append(int(input()))

w.sort(reverse=True)
for i in range(n):
    w[i] = w[i]*(i+1)

print(max(w))

