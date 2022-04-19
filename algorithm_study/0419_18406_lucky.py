N = input()
if sum(map(int, N[:len(N)//2])) == sum(map(int, N[len(N)//2:])):
    print("LUCKY")
else:
    print("READY")
