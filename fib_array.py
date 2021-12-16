numb = [0, 1]
def fib(n):
	y = 0
	z = 1
	for i in range (0,n - 1):
		x = numb[y] + numb [z]
		y = y + 1
		z = z + 1
		numb.append(x)
	return numb
result = fib(int(input()))
print (result)
