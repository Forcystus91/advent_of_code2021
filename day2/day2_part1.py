def dive():
    with open(r'C:\Users\Emilio\Documents\GitHub\advent_of_code2021\day2\day2_puzzle_input.txt') as fp:
        d = {'forward':0,'down':0,'up':0}
        string = ""
        line = fp.readline()

        while line:
            for i in range(len(line)):
                if ord(line[i]) != 32:
                    string = string + line[i]
                else:
                    d[string] += int(line[i+1])
                    break
            string = ""
            line = fp.readline()

    depth = d['down'] - d['up']
    horizontal_position = d['forward']
    return depth*horizontal_position

print(dive())