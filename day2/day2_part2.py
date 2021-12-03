def dive_with_aim():
    with open(r'C:\Users\Emilio\Documents\GitHub\advent_of_code2021\day2\day2_puzzle_input.txt') as fp:
        line = fp.readline()
        string = "" # empty string to store submarine commands
        horizontal_position = 0
        depth = 0
        aim = 0
        while line:
            for i in range(len(line)):
                if ord(line[i]) != 32:  # If the character is not equal to " ", stores the character in the string variable 
                    string = string + line[i]
                else:   # Once the command word is complete, determines the values for each variable
                    value = int(line[i+1])
                    if string == 'forward':
                        horizontal_position = horizontal_position + value
                        if aim > 0:
                            depth = depth + (value * aim)
                    elif string == 'up':
                        aim = aim - int(line[i+1])
                        if aim < 0:
                            aim = 0
                    else:
                        aim = aim + int(line[i+1])
                    string = ""
                    break
            line = fp.readline()
    return horizontal_position*depth

def main():
    print(dive_with_aim())

main()