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

    # returns the removed group
    return group_2

def solve(rows):
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
    # we are done when groups removed length is rows -1 (since 1 group left)
    groups_removed = 0

    # we now need to connect until we're done... how do we do this?
    # actually we have every single possible combination above, so should eventually
    # connect them all eventually...
    last_connections = [0, 0]
    while groups_removed < len(junction_boxes)-1:
        i1, i2 = ordered_distances[pointer][1]
        group_1 = junction_boxes[i1][1]
        group_2 = junction_boxes[i2][1]

        if group_1 != group_2:
            connect_circuits(junction_boxes, [i1, i2])
            groups_removed +=1
            last_connections = [i1,i2]

        pointer += 1

    # get unique circuit_groups
    [i1, i2] = last_connections
    return junction_boxes[i1][0][0] * junction_boxes[i2][0][0]

print(solve(rows))
