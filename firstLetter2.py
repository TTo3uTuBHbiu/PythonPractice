str = input("введите строку:").split()

firstChar = ''
prevFirstChar = ''
newStr = ''

for i in range(len(str)):
    firstChar = str[0][0]
    print(firstChar)
    newStr += prevFirstChar
    newStr += str[0][1:]
    newStr += ' '
    prevFirstChar = firstChar

newStr = prevFirstChar + newStr

print(newStr)

