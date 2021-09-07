str = input("введите строку:")
word = ''
str += ' '

count = 1
char = ''

for i in range(len(str)):
    if str[i] == ' ':
        print(word)

        for j in range(len(word)):
            for k in range(len(word)):
                if j != k:
                    if word[j] == word[k]:
                        char = word[j]
                        count += 1;

            if count != 1:
                print('Буква', char, ' повторилась', count, ' раз.')

            char = ''
            count = 1

        word = ''

    else:
        word += str[i]



