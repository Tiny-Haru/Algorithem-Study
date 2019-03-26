arrangement = input()
answer = 0
cnt = 0
for i in range(len(arrangement)):
    if arrangement[i] == '(':
        cnt = cnt + 1
    elif arrangement[i] == ')':
        if arrangement[i - 1] == "(":
            answer += (cnt - 1)
            cnt = cnt - 1
        else:
            answer = answer + 1
            cnt = cnt - 1

print(answer)
