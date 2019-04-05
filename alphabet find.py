alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dictionary = {}
for i in range(len(alphabet)):
    alphabet_dictionary[alphabet[i]] = -1

word = input()

for i in range(len(word)):
    for j in range(len(alphabet)):
        if word[i] == alphabet[j] and alphabet_dictionary[word[i]] == -1:
            alphabet_dictionary[word[i]] = i

string_to_print = ''

for i in range(len(alphabet_dictionary)):
    string_to_print += str(alphabet_dictionary[alphabet[i]]) + ' '

print(string_to_print)
