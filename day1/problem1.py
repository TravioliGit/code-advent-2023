def main(): 
    content = open('./files/day1-1.txt', 'r')
    # total1 = 0

    # for line in content:
    #     foundNumbers = []
    #     for character in line:
    #         type = character.isnumeric()
    #         if type == True:
    #             foundNumbers.append(character)
    #     lineTotal = str(foundNumbers[0]) + str(foundNumbers[len(foundNumbers)-1])
    #     total1 = total1 + int(lineTotal)
    # print(total1)

    total2 = 0
    numbersThatAreWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']  
    i = 0

    for line in content:
        foundNumbers2 = []
        i = 0
        print('og line '+line)
        for word in numbersThatAreWords:
            line = line.replace(word, str(i))
            i += 1
        print('updated line '+line)

        for character in line:
            type = character.isnumeric()
            if type == True:
                foundNumbers2.append(character)
        print('all numbers found ',foundNumbers2)
        lineTotal2 = foundNumbers2[0] + foundNumbers2[len(foundNumbers2)-1]
        print('total from line to add to running total',lineTotal2)
        total2 = total2 + int(lineTotal2)
        print('running total',total2)    
    print(total2)


if __name__ == "__main__":
    main()  