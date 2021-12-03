def main():
    print(larger_than_previous())

def larger_than_previous():
    with open(r'C:\Users\Emilio\Documents\GitHub\advent_of_code2021\day1\day1_puzzle_input.txt') as fp:
        list_of_nums = []
        line = fp.readline()
        while line:
            list = list + [int(line)]
            line = fp.readline()

    larger_num_count = 0
    for i in range(len(list) - 1):
        if list[i] < list[i+1]:
            larger_num_count +=1

    return larger_num_count

main()