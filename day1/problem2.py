def main():
    content = open('./files/day1-1.txt', 'r')
    total = 0
    numbersThatAreWords = ['oneight', 'twone', 'threeight', 'fiveight', 'sevenine', 'eightwo', 'eighthree', 'nineight', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = [18, 21, 38, 58, 79, 82, 83, 98, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for line in content:
        foundNumbers = []
        i = 0
        for word in numbersThatAreWords:
            line = line.replace(word, str(numbers[i]))
            i += 1

        for character in line:
            type = character.isnumeric()
            if type == True:
                foundNumbers.append(character)
        lineTotal = foundNumbers[0] + foundNumbers[len(foundNumbers)-1]
        total = total + int(lineTotal)
    print('total',total)

if __name__ == "__main__":
    main()  