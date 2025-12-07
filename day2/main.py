import math
import textwrap3

# looking for invalid patterns
# 1698522-1698528 contains no invalid IDs
# 446443-446449 has one invalid ID, 446446

# adding up all of the invalid IDs produces the answer

# if the range is odd-odd numbers then there are no invalid ids in there

input = ['2200670-2267527','265-409','38866-50720','7697424-7724736','33303664-33374980',
    '687053-834889','953123-983345','3691832-3890175','26544-37124','7219840722-7219900143',
    '7575626241-7575840141','1-18','1995-2479','101904-163230','97916763-98009247','52011-79060',
    '31-49','4578-6831','3310890-3365637','414256-608125','552-1005','16995-24728','6985-10895',
    '878311-912296','59-93','9978301-10012088','17302200-17437063','1786628373-1786840083',
    '6955834840-6955903320','983351-1034902','842824238-842861540','14027173-14217812']

invalid_ids = []

def loop_and_subtract(sides, sequence_tocheck):
    # sequence_tocheck = int(len(sides[0])/2)
    # part 2 were addint all integer dividers of our number length
    for j in range (1, sequence_tocheck):
        if sequence_tocheck % j == 0 and sequence_tocheck != j :
            list_to_turn_into_set = []
            print("checkable chunk len", j, sequence_tocheck)
            for i in range (int(sides[0]), int(sides[1]), 1):
                list_to_turn_into_set.append(textwrap3.wrap(str(i),j))
                # print(textwrap3.wrap(str(i),j))
                # print(list_to_turn_into_set)
                set_to_check = set(list_to_turn_into_set[0])
                # print(len(set_to_check))

                if len(set_to_check) == 1 and len(str(i))!= 1 and not i in invalid_ids: 
                    invalid_ids.append(i)
                    print(sides[0], '-', sides[1], list_to_turn_into_set, set_to_check)
                list_to_turn_into_set = []


for i in input:
    sides = str(i).split('-')
    if len(sides[0]) % 2 != 0 and len(sides[1]) % 2 != 0: # if both odd
        print(sides)
        loop_and_subtract(sides, len(sides[1]))
    # print(len(sides[0])-len(sides[1]))
    elif len(sides[0]) % 2 == 0 and len(sides[1]) % 2 == 0: # both even
        print(sides)
        loop_and_subtract(sides, int(len(sides[0])))
    else: # one even one odd - we need the even one
        if len(sides[0]) % 2 == 0 and len(sides[1]) % 2 != 0:  # len od the left side is always less or than right here
            print(sides)
            loop_and_subtract(sides, int(len(sides[0])))
        elif len(sides[0]) % 2 != 0 and len(sides[1]) % 2 == 0:
            print(sides)
            loop_and_subtract(sides, int(len(sides[1])))
    
set_ids = set(invalid_ids)
print(set_ids)
print(invalid_ids)
print(sum(set_ids))
