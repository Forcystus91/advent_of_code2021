def main():
    print(three_measure_sliding_window())

def three_measure_sliding_window():
    with open('day1.txt') as fp:
        text = fp.read()
        list = text.split()
        for i in range(len(list)):
            list[i] = int(list[i])
    
    greater_value_count = 0
    for i in range(len(list) - 3):
        val1 = list[i] + list[i+1] + list[i+2]
        val2 = val1 + list[i+3] - list[i]
        if val2 - val1 > 0:
            greater_value_count +=1

    return greater_value_count
    

main()
