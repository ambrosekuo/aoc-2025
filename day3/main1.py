f = open('input.txt', 'r')

battery_banks = []

for line in f:
	battery_banks.append(str(line.replace('\n', '')))

def find_highest_jolt(batteries):
	if len(batteries) == 1:
		return int(batteries[0])

	max_i_1 = 0
	max_i_2 = 1
	i = 1

	# basically 2 pointer, we always move to max first digit its not the last element
	# else we just check if the 2nd digit is always as high as i can get
	while i < len(batteries) -1:
		if int(batteries[max_i_1]) < int(batteries[i]) and i < len(batteries)-1:
			max_i_1 = i
			max_i_2 = i+1
		else:
			max_i_2 = i+1 if int(batteries[max_i_2]) < int(batteries[i+1]) else max_i_2
		i+=1

	return int(str(batteries[max_i_1])+str(batteries[max_i_2]))

def find_jolts(battery_banks):
	return sum([find_highest_jolt(batteries) for batteries in battery_banks])

print(find_jolts(battery_banks))
