n = int(input())
for i in range(n):
    bracket = list(input())
    while len(bracket) != 0:
        if bracket[0] == ')':
            print("NO")
            break
        else:
            if ')' in bracket:
                bracket.remove(')')
                bracket.remove('(')
            else:
                print("NO")
                break

    if len(bracket) == 0:
        print("YES")
