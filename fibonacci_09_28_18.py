class Fibonacci():
	def fib_recursive(self,n):
		if n == 0 or n == 1:
			return n

		return self.fib_recursive(n-2) + self.fib_recursive(n-1)

	def fib_iterative(self,n):
		if n == 0 or n == 1:
			return n

		fib_array = [0,1]
		for i in range(2,n+1):
			fib_array.append(fib_array[i-1]+fib_array[i-2])

		return fib_array[n] 


fibObject = Fibonacci()

print("recursive")
for i in range(0,10):
	print(fibObject.fib_recursive(i))

print("iterative")
for i in range(0,10):
	print(fibObject.fib_iterative(i))