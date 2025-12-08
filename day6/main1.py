f = open('input.txt', 'r')

rows = [] # each row has [[numbers],operator]]

operators = ['*', '+']

for line in f:
    if line[0] in operators:
        for i, char in enumerate(line.split()):
            rows[i].append(char)
    else:
        col_numbers =  line.split()
        if rows == []:
            for i in col_numbers:
                rows.append([[]])
        for i, number in enumerate(col_numbers):
            rows[i][0].append(number)

def solve(rows):
    return sum([eval(operator.join(nums)) for [nums, operator] in rows])


print(rows)
print(solve(rows))
