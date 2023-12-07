input = open("input.txt")
data = input.readlines()
input.close()

def part1():
    sum = 0
    for word in data:
        wordList = list(word)
        wordNumber = ""
        firstNum = ""
        lastNum = ""
        for char in wordList:
            if(char.isdigit()):
                firstNum = char
                break
        for char in wordList[::-1]:
            if(char.isdigit()):
                lastNum = char
                break
        wordNumber = firstNum + lastNum
        sum+= int(wordNumber)

    print(sum)

def part2():

    sum = 0
    for word in data:

        wordList = word
        wordNumber = ""
        digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
        
        numberList = []
        for i, char in enumerate(word):
            if(char.isdigit()):
                numberList.append(char)
            for value, name in enumerate(digits):
                if word[i:].startswith(name):
                    numberList.append(str(value+1))
                    break
        
        wordNumber = numberList[0] + numberList[-1]
        sum+= int(wordNumber)
    print(sum)

part2()
