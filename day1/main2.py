f = open('input.txt', 'r')

rotations = []

for line in f:
    rotations.append(str(line.replace('\n', '')))

class Dial:
    val = 50
    zeroes_found = 0

    def traverse(self, direction: str, amount: int):
        isMinus = direction == 'L'
        if isMinus:
            amount *= -1

        self.val, zeroes = rotate(self.val, amount, 0)
        self.zeroes_found += zeroes

def find_zeroes_reached(rotations):
    dial = Dial()

    for rotation in rotations:
        dial.traverse(str(rotation[0]), int(rotation[1:]))

    return dial.zeroes_found

# rotate to 0 and rotate by 100 each time after til none left
# base case + 3 cases :
# keep rotating by 100 
# keep rotating by 100
# handle case where we can't rotate fully
def rotate(position, amount, zeroes):
    if amount == 0:
        return (position, zeroes)
    
    if amount >= 100:
        return rotate(position, amount -100, zeroes +1)
    
    if amount <= -100:
        return rotate(position, amount + 100, zeroes + 1)
    
    if position == 0:
        new_position = position + amount
        return rotate((100 + new_position) % 100 if new_position < 0 else new_position % 100, 0, zeroes)

    new_position = position + amount
    if new_position >= 100:
        return rotate(new_position % 100, 0, zeroes+1)
    elif new_position <= 0:
        return rotate((100 + new_position) %100, 0, zeroes+1)
    else:
        return rotate(new_position, 0, zeroes)


print(find_zeroes_reached(rotations))
