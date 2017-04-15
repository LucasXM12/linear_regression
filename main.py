import os
import math
import linearr
import numpy as np 
import matplotlib.pyplot as plt

n = int(input("Digite o numero de dados: "))

x = []
y = []

for i in range(n):
	os.system('cls')
	x.append(float(input("Digite o " + str(i + 1) + "º dado x: ")))
	y.append(float(input("Digite o " + str(i + 1) + "º dado y: ")))

coefs = linearr.calcCoef(x, y, n)

funcX = np.arange(min(x), max(x) + 1).astype(np.double)
funcY = coefs[0] * funcX + coefs[1] 

plt.plot(x, y, 'ro', funcX, funcY)
plt.show()

os.system('cls')
print("f(x) = " + str(coefs[0]) + "x + " + str(coefs[1]))







