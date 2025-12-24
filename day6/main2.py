file_name = 'input.txt'
f = open(file_name, 'r')

# each row has [{index:number},operator]]
# index represent the digit padding, e.g. 1 has 0, 15 has 1
keyed_rows = []

operators = ['*', '+']

# lets read the length first via operators

operator_line = f.readlines()[-1]

numbers_in_each = []
operators_in_each = [operator_line[0]]
last_char = operator_line[0]
spaces_count = 0

for i, operator_char in enumerate(operator_line[1:]):
    if operator_char in operators:
        # space-1 for separator, +1 operator also takes up a column
        num_of_cols = (spaces_count-1) +1
        numbers_in_each.append(num_of_cols)
        operators_in_each.append(operator_char)
        spaces_count = 0
    else:
        spaces_count += 1


# add in last line since no operator to separate at the end
numbers_in_each.append(spaces_count)

f = open(file_name, 'r')

for i in numbers_in_each:
    keyed_rows.append({})

# A bit more confusing, but essentially, we are just grouping into an array of
# objects, where each object is the column of numbers grouped, e.g. example_input
# will look like this after:
# E.g. result of this will be:
"""
[{0: ['1', ' ', ' '], 1: ['2', '4', ' '], 2: ['3', '5', '6']},
{0: ['3', '6', '9'], 1: ['2', '4', '8'], 2: ['8', ' ', ' ']},
{0: [' ', '3', '2'], 1: ['5', '8', '1'], 2: ['1', '7', '5']},
{0: ['6', '2', '3'], 1: ['4', '3', '1'], 2: ['\n', '\n', '4']}]
"""
for line in f:
    operator_pointer = 0;
    numbers_added = 0;
    is_gap = False
    print(line)
    for i, char in enumerate(line):
        if char in operators:
            break
        if is_gap:
            is_gap = False
            continue

        if numbers_added >= numbers_in_each[operator_pointer]:
            operator_pointer += 1
            numbers_added = 0
            is_next_gap = True
        else:
            if keyed_rows[operator_pointer].get(numbers_added) is None:
                keyed_rows[operator_pointer][numbers_added] = []
            keyed_rows[operator_pointer][numbers_added].append(char)
            numbers_added+=1

# We are just looping through our grouped rows and adding the columns indices together
# to create a real number and adding the operator to this set.
# E.g.
"""
[[['1', '24', '356'], '*'], [['369', '248', '8'], '+'],
[['32', '581', '175'], '*'], [['623', '431', '4'], '+']]
"""
def convert_keyed_rows(keyed_rows, operators_in_each):
    rows = []
    for i, numbers_object in enumerate(keyed_rows):
        rows.append([[], operators_in_each[i]])
        for col_index in numbers_object:
            number_row = numbers_object[col_index]
            digits = len(number_row)
            total = ""
            for j, char in enumerate(number_row):
                if char == ' ' or char == '\n':
                    continue
                total += char
            rows[i][0].append(total)
    return rows

def solve(rows):
    return sum([eval(operator.join(nums)) for [nums, operator] in rows])

rows = convert_keyed_rows(keyed_rows, operators_in_each)
print(solve(rows))
