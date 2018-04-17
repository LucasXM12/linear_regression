import numpy as np


def calc_coef(x, y):
    n = len(x)
    sig_x = sum(x)
    sig_y = sum(y)
    sig_x2 = np.dot(x, x)
    sig_xy = np.dot(x, y)

    a = (n * sig_xy - sig_x * sig_y) / (n * sig_x2 - sig_x ** 2)
    b = (sig_y - a * sig_x) / n

    return a, b
