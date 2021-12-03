def main():
    print(larger_than_previous())

def larger_than_previous():
    with open(r'C:\Users\Emilio\Documents\GitHub\advent_of_code2021\day1\day1_puzzle_input.txt') as fp:
        list_of_values = []
        line = fp.readline()
        while line:
            list_of_values = list_of_values + [int(line)]
            line = fp.readline()

    larger_num_count = 0
    for i in range(len(list_of_values) - 1):
        if list_of_values[i] < list_of_values[i+1]:
            larger_num_count +=1

    return larger_num_count

main()