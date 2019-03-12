def push(n):
    stack.append(n)


def pop():
    try:
        print(stack.pop())
    except:
        print(-1)


def size():
    return len(stack)


def empty():
    if size() == 0:
        print(1)
    else:
        print(0)


def top():
    try:
        print(stack[-1])
    except:
        print(-1)


stack = []
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()
