n = int(input())
expr = input()
num = [0]*n
stack = []

for i in range(n):
    num[i] = int(input())

for ch in expr:
    if ch.isupper():#같은 문자가 여러번 나올 수 있음! 인덱스 순서대로만 나오는 것이 아니다.
        stack.append(num[ord(ch)-ord('A')]) #해당값은 이미 num리스트에 있을 것이므로 
    else:
        num2=stack.pop()
        num1=stack.pop()

        if ch =='+':
            stack.append(num1+num2)
        elif ch =='-':
            stack.append(num1-num2)
        elif ch == '/':
            stack.append(num1/num2)
        elif ch == '*':
            stack.append(num1*num2)

print(f'{stack[0]:.2f}')
         


