"""
Bootstrapping is the process of generating simulated samples by repeatedly drawing with replacement
from an existing sample.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import resample
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load data set
badDrivers = pd.read_csv('bad-drivers.csv')

# Create bootstrap samples and collect errors
bootstrapErrors = []
for i in range(0, 30):
    # Create the bootstrap sample and the out-of-bag sample
    boot = resample(badDrivers, replace=True, n_samples=51)
    oob = badDrivers[~badDrivers.index.isin(boot.index)]

    # Fit a linear model to the bootstrap sample
    XBoot = boot[
        ['Losses incurred by insurance companies for collisions per insured driver ($)']
    ].values.reshape(-1, 1)
    yBoot = boot[['Car Insurance Premiums ($)']].values.reshape(-1, 1)
    linModel = LinearRegression()
    linModel.fit(XBoot, yBoot)

    # Predict y values for the out-of-bag sample
    XOob = oob[
        ['Losses incurred by insurance companies for collisions per insured driver ($)']
    ].values.reshape(-1, 1)
    YOob = oob[['Car Insurance Premiums ($)']].values.reshape(-1, 1)
    YOobPredicted = linModel.predict(XOob)

    # Calculate the error
    bootError = mean_squared_error(YOob, YOobPredicted)
    bootstrapErrors.append(bootError)

# Mean of Errors
np.mean(bootstrapErrors)
# Standard deviation of errors
np.std(bootstrapErrors)

# Plot the errors
plt.plot(bootstrapErrors, np.zeros_like(bootstrapErrors), '.')
plt.xlabel('Bootstrap errors (MSE)', fontsize=14)
plt.gca().axes.yaxis.set_ticks([])

