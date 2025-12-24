import copy

f = open('input.txt', 'r')

tree = []

for line in f:
    row = list(line)
    tree.append(row)

# side effect
def draw_tree(tree):
    for line in tree:
        for char in line:
            print(char, end="")

def draw_tree_replace(tree):
    import os, time
    os.system("cls" if os.name == "nt" else "clear")
    for row in tree:
        print("".join(str(x) for x in row))
    time.sleep(0.05)

# def draw_tree_replace(tree):
#     import sys, time
#     sys.stdout.write("\x1b[2J")  # clear screen once
#     sys.stdout.flush()
#
#     sys.stdout.write("\x1b[H")
#     for row in tree:
#         sys.stdout.write("".join(str(x) for x in row) + "\n")
#     sys.stdout.flush()
#     time.sleep(0.05)

# question is do we update the array? probably on first attempt...

# we find s and draw the line at the bottom
def get_first_beam(tree):
    updated_tree = copy.deepcopy(tree)
    # can just safely assume it's in the first row, since we can see both
    # our inputs
    s_row = {x: i for i,x in enumerate(updated_tree[0])}
    pos_of_s = s_row.get('S')
    return (1, pos_of_s)

# we are done when we found any beams in the last row
def is_timeline_done(tree):
    last_row = tree[-1]
    return len([char for char in last_row if char == '|']) > 0

# Part B, maybe the key here with the low count is there are many branches
# where there are no more splits. Thats why example should be so low at 40
# timelines?
def get_splt_tree(tree):
    [level, beam_index] = get_first_beam(tree)
    level = level+1
    # type will be a tuple containing beams and splits per beam
    beams = [(beam_index, 1)]

    while level < len(tree):
        row = tree[level]
        for i, [beam_index, splits] in enumerate(beams):
            if row[beam_index] == '^':
                beams[i] = [beam_index-1, splits]
                beams.append((beam_index+1, splits))

        # collect the beams that are the same
        beams_map = {}
        for [beam_index, splits] in beams:
            beams_map[beam_index] = beams_map.get(beam_index, 0) + splits
        beams = [(beams_index, beams_map[beams_index]) for beams_index in beams_map]

        level +=1

    return sum([splits for [_, splits] in beams])


print(get_splt_tree(tree))


"""
 What makes what we had built via A quite ineffiicent is that we keep track of every
 split as its own timeline. But we really only care about how many paths reaches
 a point.
 E.g. if 5 paths hit a splitter, we just now have 10 paths. But we don't actually
 need to know how they get there. So we just need to keep track of splits
 per trachyon beam.
"""
