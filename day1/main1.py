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
		# because our spin can go multiple times around, we need to find
		# remainder/amount divided by
		# e.g. -399 is my value
		# -399 // 100 = 3, -399 % 100 = -99
		# So, we end up beLow 0 by 99. Which I need to do 100-99 = 1
		# Need to also handle when it is 100

		position = result % 100
		self.val = position if position >= 0 else 100-position

		if self.val == 0:
			self.zeroes_found +=1

def find_zeroes_reached(rotations):
	dial = Dial()

	for rotation in rotations:
		dial.traverse(str(rotation[0]), int(rotation[1:]))

	return dial.zeroes_found

print(find_zeroes_reached(rotations))
