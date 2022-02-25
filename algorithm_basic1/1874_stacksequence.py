n=int(input())
count = 0
result = []
st = []
result_msg = True
for i in range(n):
    s = int(input())
    while count < s:#while문이므로 조건에 해당하는게 한 번 돌고나서 탈출함 그래서 count수가 스택에 저장됨
        count +=1 #count는 안줄어든다! 다음 숫자가 입력되도 다음 숫자부터 스택에 쌓을 수 있다.
        st.append(count)
        result.append('+')
    
    if st[-1]==s:
        st.pop()
        result.append('-')
    else:
        result_msg = False

if result_msg is False:
    print("NO")
else:
    print("\n".join(result))