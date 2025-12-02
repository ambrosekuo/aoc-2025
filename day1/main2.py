f = open('example_input.txt', 'r')

rotations = []

for line in f:
    rotations.append(str(line.replace('\n', '')))

class Dial:
    val = 50
    zeroes_found = 0

    def traverse(self, direction: str, amount: int):
        isMinus = direction == 'L'
        if isMinus:
            amount = amount * -1

        result = self.val + amount
        print(result)
        # We really are just counting the divisons now
        # ugly LOGIC, if we were at 0 and we move left or right, still didnt hit 0
        if self.val == 0 and (result < 100 and result > -100):
            zeroes_found_duration_rotation = 0
        elif self.val != 0 and result == 0:
            zeroes_found_duration_rotation = 1
        else:
            zeroes_found_duration_rotation = abs(result // 100)

        print('zeroes_found_duration_rotation', zeroes_found_duration_rotation)
        self.val = result % 100
        print('new dial', self.val)

        self.zeroes_found += zeroes_found_duration_rotation

def find_zeroes_reached(rotations):
    dial = Dial()

    for rotation in rotations:
        dial.traverse(str(rotation[0]), int(rotation[1:]))

    return dial.zeroes_found

print(find_zeroes_reached(rotations))
