f = open('input.txt', 'r')

ranges= []
# just one line i think
for line in f:
    ranges = [raw_ranges.split('-') for raw_ranges in line.split(',')]

# ensure ranges are input
ranges = [[int(range[0]), int(range[1])] for range in ranges]

def is_invalid(num):
    [num1, num2] = [str(num)[:len(str(num))//2],str(num)[len(str(num))//2:]]
    return num1 == num2

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
