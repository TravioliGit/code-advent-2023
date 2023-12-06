def main(): 
    content = open('./files/day1-1.txt', 'r')
    total = 0

    for line in content:
        foundNumbers = []
        for character in line:
            type = character.isnumeric()
            if type == True:
                foundNumbers.append(character)
        lineTotal = str(foundNumbers[0]) + str(foundNumbers[len(foundNumbers)-1])
        total = total + int(lineTotal)
    print('total',total)

if __name__ == "__main__":
    main()  