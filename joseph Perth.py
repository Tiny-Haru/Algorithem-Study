import sys

num, cycle = input().split()
queue = []

num = int(num)
cycle = int(cycle)

for i in range(1, num + 1):
    queue.append(i)

sys.stdout.write("<")
for i in range(num):
    for j in range(cycle - 1):
        queue.append(queue[0])
        queue.pop()
    sys.stdout.write(str(queue[0]))
    queue.pop()
    if i != num:
        sys.stdout.write(", ")

sys.stdout.write(">")
