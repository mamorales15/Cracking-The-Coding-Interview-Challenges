savedFibonacci = dict()

def fibonacci(n):
	if n in savedFibonacci:
		return savedFibonacci[n]
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		currFib = fibonacci(n - 1) + fibonacci(n - 2)
		savedFibonacci[n] = currFib
		#print savedFibonacci
		return currFib

n = int(input())
print(fibonacci(n))