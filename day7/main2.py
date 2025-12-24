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
def draw_starting_frame(tree):
    updated_tree = copy.deepcopy(tree)
    # can just safely assume it's in the first row, since we can see both
    # our inputs
    s_row = {x: i for i,x in enumerate(updated_tree[0])}
    pos_of_s = s_row.get('S')
    updated_tree[1][pos_of_s] = '|'

    return updated_tree

# we are done when we found any beams in the last row
def is_timeline_done(tree):
    last_row = tree[-1]
    return len([char for char in last_row if char == '|']) > 0

# Part B, maybe the key here with the low count is there are many branches
# where there are no more splits. Thats why example should be so low at 40
# timelines?
def get_splt_tree(tree):
    updated_tree = draw_starting_frame(tree)
    level = 2 # note level starts at 0
    split_count = 0
    timelines = [updated_tree]

    # the key here is that we can travel through all timelines at the same level
    # at a time
    while level < len(updated_tree):
        # will update current timelines, but also iterate through tracked ones
        timelines += update_all_next_split_frames(timelines, level)
        print(len(timelines))
        # print(len(timelines))
        level +=1

    # for timeline in timelines:
    #     draw_tree(timeline)

    return len(timelines)

def update_all_next_split_frames(timelines, level):
    new_timelines = []
    for tree in timelines:
        new_timelines += update_next_split_frame(tree, level)

    return new_timelines

# side effect
def update_next_split_frame(tree, level):
    previous_row = tree[level-1]
    row = tree[level]
    splitters = [(i, x) for i,x in enumerate(row) if x == '^']
    beams = [(i, x) for i,x in enumerate(previous_row) if x == '|']

    new_timelines = []

    for [beam_i, beam] in beams:
        # will assume that adjacents don't have splitters and empty space
        # no ask in problem to handle this
        # also will assume out of bounds doesn't exist
        if row[beam_i] == '^':
            new_timeline_tree = copy.deepcopy(tree)
            # lets keep this as the current timeline of this tree
            row[beam_i-1] = '|'
            # new_timeline
            new_timeline_row = new_timeline_tree[level]
            new_timeline_row[beam_i+1] = '|'

            new_timelines.append(new_timeline_tree)
        else:
            row[beam_i] = '|'

    return new_timelines

print(get_splt_tree(tree))
