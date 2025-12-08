f = open('example_input.txt', 'r')

# each row has [{index:number},operator]]
# index represent the digit padding, e.g. 1 has 0, 15 has 1
keyed_rows = []

operators = ['*', '+']

for line in f:
    if line[0] in operators:
        for i, char in enumerate(line.split()):
            keyed_rows[i].append(char)
    else:
        # we cant use split, we need to look ahead when we ended
        row_number = -1

        for line_i, char in enumerate(line):
            if row_number >= 0 and line_i +1 <= len(line) and char == ' ' and line[line_i+1]:
                line

        if keyed_rows == []:
            for i in col_numbers:
                keyed_rows.append([{}])
        for i, number in enumerate(col_numbers):
            digits = len(number)
            for number_index, char in enumerate(number):
                digit_padding = digits-(number_index+1)
                if keyed_rows[i][0].get(digit_padding) is None:
                    keyed_rows[i][0][digit_padding] = ""
                keyed_rows[i][0][digit_padding] += char

def convert_keyed_rows(keyed_rows):
    rows = []
    for [keyed_row, operator] in keyed_rows:
        row = []
        for key in keyed_row:
            row.append(keyed_row[key])
        rows.append([row, operator])
    return rows

def solve(rows):
    return sum([eval(operator.join(nums)) for [nums, operator] in rows])

print(keyed_rows)
rows = convert_keyed_rows(keyed_rows)
#
print(rows)
print(solve(rows))
