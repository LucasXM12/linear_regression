def calcCoef(x, y, n):
	sigX = sum(x)
	sigY = sum(y)
	sigX2 = calcSumX2(x, n)
	sigXY = calcSumXY(x, y, n)

	a = (n * sigXY - sigX * sigY) / (n * sigX2 - sigX ** 2)
	b = (sigY - a * sigX) /	n

	return [a, b]

		
def calcSumXY(x, y, n):
	ret = 0

	for i in range(n):
		ret += x[i] * y[i]
		
	return ret

def calcSumX2(x, n):
	ret = 0

	for i in range(n):
		ret += x[i] ** 2

	return ret


 

		