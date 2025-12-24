import copy

f = open('example_input.txt', 'r')

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

# after all the splits
def get_splt_tree(tree):
    updated_tree = draw_starting_frame(tree)
    print(len(updated_tree))
    level = 2 # note level starts at 0
    split_count = 0

    # ok i would prefer to use no side effects, but seems crazy to deep copy per
    # frame
    while level < len(updated_tree):
        split_count += update_next_split_frame(updated_tree, level)
        draw_tree_replace(updated_tree)
        level +=1


    return split_count

# side effect
def update_next_split_frame(tree, level):
    split_count = 0
    previous_row = tree[level-1]
    row = tree[level]
    splitters = [(i, x) for i,x in enumerate(row) if x == '^']
    beams = [(i, x) for i,x in enumerate(previous_row) if x == '|']

    for [beam_i, beam] in beams:
        # will assume that adjacents don't have splitters and empty space
        # no ask in problem to handle this
        # also will assume out of bounds doesn't exist
        if row[beam_i] == '^':
            row[beam_i-1] = '|'
            row[beam_i+1] = '|'
            split_count +=1
        else:
            row[beam_i] = '|'

    return split_count

print(get_splt_tree(tree))
