print("hello")

#string & printing
msg = "hello message"
print(msg)

print("")

#arrays & indexes
bikes = ["red", "green", "blue"]
print(bikes)
print(bikes[0])
print(bikes[-1])
print(bikes[-2])

print("")

#modulus
for i in range(0,4):
	print(bikes[i%3])

print("")

#len = length of  array => 0 to 3
for i in range(0,4):
	print((bikes[i%len(bikes)]))

print("")

#tuples
my_tuple = (2,20,5,"red")
print(my_tuple)
print(my_tuple[1])





