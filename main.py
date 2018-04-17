import os

import matplotlib.pyplot as plt
import numpy as np

import linearr

n = int(input("Digite o número de dados: "))

x = []
y = []

for i in range(n):
    os.system('cls')
    x.append(float(input("Digite o %iº dado x: " % (i + 1))))
    y.append(float(input("Digite o %iº dado y: " % (i + 1))))

coefs = linearr.calc_coef(x, y)

funcX = np.arange(min(x), max(x) + 1).astype(np.double)
funcY = coefs[0] * funcX + coefs[1]

plt.plot(x, y, 'ro', funcX, funcY)
plt.show()

os.system('cls')
print("f(x) = %fx + %f" % tuple(coefs))
