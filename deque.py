import sys


class dequeue():
    def __init__(self):
        self.my_list = []
        self.size = 0

    def push_front(self, item):
        self.my_list.insert(0, item)
        self.size += 1

    def push_back(self, item):
        self.my_list.append(item)
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.my_list.pop(0)

    def pop_back(self):
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.my_list.pop(-1)

    def my_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        else:
            return self.my_list[0]

    def back(self):
        if self.size == 0:
            return -1
        else:
            return self.my_list[-1]


if __name__ == '__main__':
    d = dequeue()
    t = int(sys.stdin.readline())
    for _ in range(t):
        command = sys.stdin.readline().split()
        if command[0] == 'push_back':
            d.push_back(command[1])
        elif command[0] == 'push_front':
            d.push_front(command[1])
        elif command[0] == 'front':
            sys.stdout.write(str(d.front()))
            sys.stdout.write('\n')
        elif command[0] == 'back':
            sys.stdout.write(str(d.back()))
            sys.stdout.write('\n')
        elif command[0] == 'size':
            sys.stdout.write(str(d.my_size()))
            sys.stdout.write('\n')
        elif command[0] == 'empty':
            sys.stdout.write(str(d.empty()))
            sys.stdout.write('\n')
        elif command[0] == 'pop_front':
            sys.stdout.write(str(d.pop_front()))
            sys.stdout.write('\n')
        elif command[0] == 'pop_back':
            sys.stdout.write(str(d.pop_back()))
            sys.stdout.write('\n')
