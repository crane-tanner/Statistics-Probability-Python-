import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

#
# rand.seed(0) # Set the seed to 0
#
# gauss = []
#
# # normal dist with mean 0 and std dev of 1
# # puts numbers in the list with append
# for i in range(1000):
#     gauss.append(rand.gauss(0, 1))
#
# # create a histogram from list
# plt.hist(gauss)
# plt.title("Normal Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


# set seed to input
num = int(input())
np.random.seed(num)

# randomly generate 500 numbers between 0 and 100 using the linspace function
x = np.linspace(0, 100, 500)
# randomly generate 500 numbers from the normal distribution with mean = 0 and sd = 1
noise = np.random.normal(0, 1, 500)

y = x + noise # sum of x and noise

model = st.linregress(x, y) # create a linear regression model using scipy.stats

print(model)

plt.plot(x,y)
plt.title("Linear Regression Model")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.show()
