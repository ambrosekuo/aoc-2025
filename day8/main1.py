f = open('input.txt', 'r')

rows = []
for line in f:
    rows.append([int(number.strip()) for number in line.split(',')])


def get_distance(cord1, cord2):
    import math
    [x1,y1,z1] = cord1
    [x2,y2,z2] = cord2

    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def connect_circuits(junction_boxes, circuits_to_connect):
    group_1 = junction_boxes[circuits_to_connect[0]][1]
    group_2 = junction_boxes[circuits_to_connect[1]][1]

    # lets just make all group_2 same as group 1
    for i, [_, group] in enumerate(junction_boxes):
        if group == group_2:
            junction_boxes[i][1] = group_1

    return junction_boxes

def solve(rows, connections):
    junction_boxes = [[row, i] for i, row in enumerate(rows)]
    distances = []

    # build the sorted distances
    for i, [cord1, group1] in enumerate(junction_boxes):
        for j, [cord2, group2] in enumerate(junction_boxes[i+1:]):
            if group1 == group2:
                # already connected, skipping
                continue
            current_distance = get_distance(cord1, cord2)
            distances.append([current_distance, [i, i+j+1]])

    distances.sort(key=lambda distance: distance[0])
    ordered_distances = distances
    pointer = 0
    current_connections = 0
    while current_connections < connections:
        i1, i2 = ordered_distances[pointer][1]
        group_1 = junction_boxes[i1][1]
        group_2 = junction_boxes[i2][1]

        if group_1 != group_2:
            connect_circuits(junction_boxes, [i1, i2])

        current_connections += 1
        pointer += 1

    # get unique circuit_groups
    unique_map = {}
    for [_, group] in junction_boxes:
        if unique_map.get(group) is None:
            unique_map[group] = 0
        unique_map[group] += 1
    # multiply together to solve
    group_counts = [unique_map[group] for group in unique_map]
    group_counts_desc = sorted(group_counts, reverse=True)

    return group_counts_desc[0] * group_counts_desc[1] * group_counts_desc[2]

print(solve(rows, 1000))
