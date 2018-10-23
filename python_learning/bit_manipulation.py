number = 0 
other_number = 5
other_number_2 = 12

number ^= other_number #XOR 0000 => 0101
print(number)

number <<= 1	#Shift bit to left, 0101 => 1010
print(number)

number >>= 1  #Shift bit to right, 1010 => 0101
print(number)

number = other_number ^ other_number_2 #XOR 0101 ^ 1100 => 1001
print(number)

number = other_number & other_number_2 #AND 0101 & 1100 => 0100
print(number)

number = other_number | other_number_2 #OR 0101 % 1100 => 1101
print(number)
