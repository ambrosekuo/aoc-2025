f = open('input.txt', 'r')

map = []

for line in f:
    row = []
    for char in line:
        if char != '\n':
            row += char
    map.append(row)

def get_tile(map, i, j):
    max_i = len(map) - 1
    max_j = len(map[0]) -1
    if i == -1 or j == -1 or i > max_i or j > max_j:
        return '.'
    return map[i][j]

surrounding_delta = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

def is_surrounding_under_four(map, i, j):
    nearby_paper_towels = 0
    for [di, dj] in surrounding_delta:
        if get_tile(map, i+di, j+dj) == '@':
            nearby_paper_towels +=1

    return nearby_paper_towels < 4

def count_valid_paper_towels(map):
    counts = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@' and is_surrounding_under_four(map, i, j):
                counts +=1

    return counts

print(map)
print(count_valid_paper_towels(map))
