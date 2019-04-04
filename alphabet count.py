alphabet = [0] * 100
string = input()

for i in range(len(string)):
    for j in range(26):
        if string[i] == chr(ord('a') + j):
            alphabet[j] += 1

for i in range(26):
    print(str(alphabet[i]) + " ", end='')
