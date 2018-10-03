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

	def find_stolen_copter_answer(self):
		unique_delivery_id = 0

		for i in self.delivery_ids:
			unique_delivery_id ^= i 

		return unique_delivery_id

quadObject = Quadcopter()
print("My solution")
print(quadObject.find_stolen_copter())
print("Their solution")
print(quadObject.find_stolen_copter())



