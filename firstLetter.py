str = input("введите строку:")
str += ' '

newStr = ''
word = ''
firstChar = ''
prevFirstChar = ''

for i in range(len(str)):
    if str[i] == ' ':
        print(word)

        for j in range(len(word)):
            firstChar = word[0]
            newStr += prevFirstChar
            newStr += word[1:]
            newStr += ' '
            prevFirstChar = firstChar
            break

        word = ''

    else:
        word += str[i]

newStr = prevFirstChar + newStr

print(newStr)
