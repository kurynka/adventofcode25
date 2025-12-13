
lines = open('/Users/kalinka/adventofcode25/day3/input.txt').read().splitlines()


print(len(lines))
# joltage detector, need to detect biggest digit, store the position
# then detect the second biggest with index bigger than the first biggest
# arrange them into a number 
# sum jotlages from each bank (line)

# pos_to_ignore = 0
total_joltage = 0

for line in lines:
    # print(len(line))
    highest_pos = 0
    second_highest_pos = 0
    joltage = ''
    highest_number = 0
    second_highest_number = 0
    for i in range (0, len(line)-1, 1):
        # print('checking', line[i])
        if int(line[i]) > highest_number:
            if int(line[i]) == 99: print('last digit')
            highest_number = int(line[i])
            highest_pos = i
            # print('assigned', i)
    for j in range(highest_pos + 1, len(line), 1):
        if int(line[j]) > second_highest_number:
            # if highest_pos == 99: print('checking from range ', highest_pos +1)
            second_highest_number = int(line[j])
            # print(second_highest_number)
            second_highest_pos = j
    joltage = line[highest_pos] + line[second_highest_pos]
    num_joltage = int(joltage)
    # print(line)
    # print(num_joltage)
    total_joltage += num_joltage

print(total_joltage)

        
