def dive_with_aim():
    with open(r'C:\Users\Emilio\Documents\GitHub\advent_of_code2021\day2\day2_puzzle_input.txt') as fp:
        line = fp.readline()
        horizontal_position = 0
        depth = 0
        aim = 0
        string = ""
        while line:
            for i in range(len(line)):
                if ord(line[i]) != 32:
                    string = string + line[i]
                else:
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
            line = fp.readline()
    
    print(horizontal_position)
    print(depth)
    return horizontal_position*depth

def main():
    print(dive_with_aim)

main()