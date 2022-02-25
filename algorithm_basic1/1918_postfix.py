expr = input()
stack = []
ans = []

for ch in expr:
    if ch.isalpha():
        ans.append(ch)
    else:
        if ch == '(':
            stack.append(ch)
        elif ch == '*' or ch == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/' ):
                ans.append(stack.pop())
            stack.append(ch)
        elif ch == '+' or ch == '-':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
while stack:
    ans.append(stack.pop())
print(''.join(ans))