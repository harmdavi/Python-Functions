def sayHello():
    return "Hello There!"

def simpConvert(inputString):
    #TODO I Need to add a function that allows for base f
    string = ''
    numb = ''
    unit = ''
    mult = 0
    percount = 0
    invalid = [['wrong data was inserted inot the simpConvert function']]
    for char in inputString:
        print(char)
        if char.isdigit():
            numb = numb + char
        elif char == '.':
            percount = percount +1
            if percount > 1:
                
                return invalid
            numb = numb + char
        else:
            string = string + char
            if char == 'p':
                mult = -12
            elif char == 'n':
                mult = -9
            elif char == 'u':
                mult = -6
            elif char == 'm':
                mult = -3
            elif char == 'k':
                mult = 3
            elif char == 'M':
                mult = 6
            elif char == 'G':
                mult = 9
            elif char == 'T':
                mult = 12
            elif char == 'V' or char =='v':
                unit = 'V'
            elif char == 'A' or char == 'a':
                unit = 'A'
            elif char == 'R' or char =='r':
                unit = 'R'
            elif char == 'W' or char == "w":
                unit = 'W'
            elif char == ' ':
                pass
            else:
                return invalid

    
    answer = [[numb],[string],[mult],[unit] ]
    return answer
