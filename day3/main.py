lines = open('/Users/kalinka/adventofcode25/day3/input.txt').read().splitlines()


# print(len(lines))
# joltage detector, need to detect biggest digit, store the position
# then detect the second biggest with index bigger than the first biggest, 12 positions
# arrange them into a number 
# sum jotlages from each bank (line)

total_joltage = []


for line in lines:
    print(line)
    battery = []
    # print(len(line))

    previous_digit = 0
    position_to_start = 0
    for i in range (0, 12): # going in 12 times and looking for highest joltage
        highest_num = 0
        for j in range (position_to_start, len(line)-11+i): # going in the rest of digits
            # print('pos to start from ', position_to_start)
            if int(line[j]) > highest_num:
                highest_num = int(line[j])
                # print('found highest num- ', highest_num, 'pos- ', j)
                position_to_start = j + 1 
        battery.append(highest_num)
    total_joltage.append(int(str(battery).replace('[','').replace(', ', '').replace(']', '')))

print(sum(total_joltage))


        
