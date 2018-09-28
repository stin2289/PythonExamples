class Quadcopter():
	def __init__(self):
		self.delivery_ids = [1,1,2,2,5,4,6,7,7,6,4]

	def find_stolen_copter(self):
		ids_set = set()
		for i in self.delivery_ids:
			if i in ids_set:
				ids_set.remove(i)
			else:
				ids_set.add(i)

		return ids_set.pop()

quadObject = Quadcopter()
print(quadObject.find_stolen_copter())
