#Classic Knapsack problem
class CakeThief():

	def max_duffell_bag_value_recursive(self,cakes,max_weight):
		if max_weight <= 0:
			return 0

		max_value = 0
		for cake in cakes:
			if cake[0] == 0 or cake[1] == 0:
				print("Invalid cake weight or value")
				return 0

			new_max_weight = max_weight - cake[0]
			if new_max_weight >= 0:
				max_value = max(cake[1] + self.max_duffell_bag_value_recursive(cakes,new_max_weight),max_value)

		return max_value


	# def max_duffell_bag_value_dp(self,cakes,max_weight):
	# 	if max_weight <= 0:
	# 		return 0

	# 	weights = []
	# 	weight_index = 1

	# 	while weight_index <= max_weight:

	# 		current_max_value_at_weight = 0
	# 		for weight,value in cakes:
	# 			if weight == weight_index:
	# 				current_max_value_at_weight = max(current_max_value_at_weight,value)

	# 		weights.append(current_max_value_at_weight)


	# 	max_value = 0
	# 	weight_leftover = max_weight

	# 	while weight_leftover > 0:

			


	# 	return current_max_value_at_weight



cake_tuples = [(7,160),(3,90),(2,15)]
capacity = 20

cake_tuples_2 = [(7,160),(3,90),(2,15)]
capacity_2 = 0

cake_tuples_3 = [(0,160),(3,90),(2,15)]
capacity_3 = 10

cakeThiefObject = CakeThief()
print(cakeThiefObject.max_duffell_bag_value_recursive(cake_tuples,capacity))
print(cakeThiefObject.max_duffell_bag_value_recursive(cake_tuples_2,capacity_2))
print(cakeThiefObject.max_duffell_bag_value_recursive(cake_tuples_3,capacity_3))


print("\nDP solution\n")

# cake_tuples_4 = [(7,160),(3,90),(2,15)]
# capacity_4 = 15
# print(cakeThiefObject.max_duffell_bag_value_dp(cake_tuples_4,capacity_4))