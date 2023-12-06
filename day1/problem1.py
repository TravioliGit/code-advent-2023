def main(): 
    content = open('./files/day1-1.txt', 'r')
    content2 = open('./files/day1-1.txt', 'r')
    total1 = 0

    for line in content:
        foundNumbers = []
        for character in line:
            type = character.isnumeric()
            if type == True:
                foundNumbers.append(character)
        lineTotal = str(foundNumbers[0]) + str(foundNumbers[len(foundNumbers)-1])
        total1 = total1 + int(lineTotal)
    print('total',total1)

    total2 = 0
    numbersThatAreWords = ['oneight', 'twone', 'threeight', 'fiveight', 'sevenine', 'eightwo', 'eighthree', 'nineight', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [18, 21, 38, 58, 79, 82, 83, 98, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for line2 in content2:
        foundNumbers2 = []
        i = 0
        for word2 in numbersThatAreWords:
            line2 = line2.replace(word2, str(numbers[i]))
            i += 1

        for character2 in line2:
            type2 = character2.isnumeric()
            if type2 == True:
                foundNumbers2.append(character2)
        lineTotal2 = foundNumbers2[0] + foundNumbers2[len(foundNumbers2)-1]
        total2 = total2 + int(lineTotal2)
    print('total2',total2)

if __name__ == "__main__":
    main()  