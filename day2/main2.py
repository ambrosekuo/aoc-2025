import math
f = open('input.txt', 'r')

ranges= []
for line in f:
    ranges = [raw_ranges.split('-') for raw_ranges in line.split(',')]

ranges = [[int(range[0]), int(range[1])] for range in ranges]

def is_invalid(num):
    num = str(num)
    i = 0
    if len(num) == 1:
        return False
    while i < math.ceil(len(num) / 2):
        if all('' == splits for splits in num.split(num[:i+1])):
            print(num)
            return True

        i+=1
    return False

def get_invalid_numbers(ranges):
    invalid = []
    for [lower, higher] in ranges:
        i = lower
        while i <= higher:
            if is_invalid(i):
                invalid.append(i)
            i+=1

    return invalid

print(sum(get_invalid_numbers(ranges)))
