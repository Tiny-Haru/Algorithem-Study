num = int(input())
input_list = []

input_list.insert(0, 0)
input_list.insert(1, 1)
input_list.insert(2, 2)
input_list.insert(3, 4)

for i in range(0, num):
    n = int(input())
    for j in range(4, n + 1):
        input_list.insert(j, input_list[j - 1] + input_list[j - 2] + input_list[j - 3])
    print(input_list[n])
