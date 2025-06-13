import random as rand
import numpy as np
import matplotlib.pyplot as plt

"Method to approximate pi. Formula for error = |pi_approx - pi| / pi"

def pi_approx(num):
    rand.seed(0)
    points = 0
    for _ in range(num):
        x = rand.uniform(0,1)
        y = rand.uniform(0,1)
        if x**2 + y**2 < 1:
            points += 1
    return points*4/num

approx = pi_approx(10000)
print("Approximation:",approx)
print("Error:", np.abs(approx - np.pi)/np.pi)

samples = np.logspace(1,5)

approx_list = []

for i in samples:
    approx_list.append(pi_approx(int(i)))

errors = []

for i in approx_list:
    errors.append(np.abs(i - np.pi)/np.pi)

plt.xscale("log")
plt.minorticks_off()
plt.title("Error rates of the Monte Carlo \n simulation approximating pi", fontsize=20)
plt.xlabel("Samples", fontsize=12)
plt.ylabel("Error", fontsize=12)
plt.plot(samples, errors)
plt.show()

