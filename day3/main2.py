f = open('input.txt', 'r')

battery_banks = []

for line in f:
	battery_banks.append(str(line.replace('\n', '')))

# We always want the highest number starting from first digit.
# So if we know that we need to fill out x numbers after, we can just have
# a trailing limit that we cut off. Then look for the highest in that range.
# Once found, we have the "rest" range and keep going til done.
def find_highest_within(batteries, trailing_limit):
    if trailing_limit == 0:
        return str(max([int(battery) for battery in batteries]))

    sub_batteries = batteries[:len(batteries)-trailing_limit]
    max_i = 0
    i = 0
    while i < len(sub_batteries):
        if int(sub_batteries[i]) > int(sub_batteries[max_i]):
            max_i = i
        i+=1
    # print(trailing_limit, sub_batteries[max_i], max_i, batteries[max_i+1:])
    return sub_batteries[max_i]+ find_highest_within(batteries[max_i+1:], trailing_limit-1)

def find_highest_jolt(batteries):
    return find_highest_within(batteries, 11)

def find_jolts(battery_banks):
	return sum([int(find_highest_jolt(batteries)) for batteries in battery_banks])

print(find_jolts(battery_banks))
