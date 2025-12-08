f = open('input.txt', 'r')

ranges = []
available = []
is_answer = False

for line in f:
    if line == '\n':
        is_answer = True
        continue

    if is_answer:
        available.append(int(line.strip()))
    else:
        [low, high] = line.strip().split('-')
        ranges.append([int(low), int(high)])

# available = [item for item in available]
# print(ranges)
# print(available)

def build_fresh_map(ranges):
    fresh_map = {}
    for [low, high] in ranges:
        while low <= high:
            if fresh_map.get(low) is None:
                fresh_map[low] = 0
            fresh_map[low] += 1
            low +=1

    return fresh_map

def check_range(ranges, item):
    for [low, high] in ranges:
        if item >= low and item <= high:
            return True

    return False

def get_fresh_count(ranges, available):
    # fresh_map = build_fresh_map(ranges)
    count = 0
    for item in available:
        # if fresh_map.get(item) is not None:
        if check_range(ranges, item):
            count +=1
    return count

print(get_fresh_count(ranges, available))
