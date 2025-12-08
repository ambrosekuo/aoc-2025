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


def combine_range(range1, range2):
    [low1, high1] = range1
    [low2, high2] = range2

    # if range1 overlaps with range2
    if (low1 >= low2 and low1 <= high2) or (high1 >= low2 and high1 <= high2) or (low2 >= low1 and low2 <= high1) or (high2 >= low1 and high2 <= high1):
        return [min(low1, low2), max(high1,high2)]

    return None

# key idea is as soon as there is overlap, you can combine the range
def find_fresh_counts(ranges):
    has_combined_at_all = True # do while, but do while in 2025 is crazy

    # Outer while loop becauase even if we combine a range, the new range
    # can still overlap with our existing ranges. So let's keep checking within
    # our unique_ranges until we haven't found combinations anymore.
    while has_combined_at_all is True:
        unique_ranges = [ranges[0]]

        has_combined_at_all = False
        for range1 in ranges[1:]:
            has_combined = False
            for index, range2 in enumerate(unique_ranges):
                maybe_combined = combine_range(range1, range2)
                if maybe_combined is not None:
                    unique_ranges.pop(index)
                    unique_ranges.append(maybe_combined)
                    has_combined= True
                    has_combined_at_all = True

            if not has_combined:
                unique_ranges.append(range1)

        ranges = unique_ranges

    total_fresh = 0
    for [low, high] in unique_ranges:
        total_fresh += high-low +1

    return total_fresh

print(find_fresh_counts(ranges))
