from numpy import linalg as LA
import pandas as pd
from sklearn.decomposition import PCA

"""
Lab for calculating eigenvalues and eigenvectors from the correlation matrix 

fires = pd.read_csv("forestfires.csv")  # read in forestfires.csv

X = pd.DataFrame(fires, columns=["FFMC", "DMC", "DC", "ISI", "temp", "RH", "wind",
                                 "rain"])
# create a new data frame with the columns FFMC, DMC, DC, ISI, temp, RH,
# wind, and rain, in that order.

X_corr = X.corr()   # calculate the correlation matrix for the data in the data frame X

w, v = LA.eig(X_corr)  # calculate the eigenvalues and eigenvectors of the matrix X_corr

print(w, v)

"""


fires = pd.read_csv("forestfires.csv") # read in forestfires.csv

X = pd.DataFrame(fires, columns=["FFMC", "DMC", "DC", "ISI", "temp", "RH", "wind", "rain"])

# create a new dataframe with the columns FFMC, DMC, DC, ISI, temp, RH, wind, and rain, in that order


X_cov = X.cov() # calculate the covariance matrix

w,v = LA.eig(X_cov) # calculate the eigenvalues and eigenvectors of matrix X_cov

pca = PCA()
pca.fit(X)

var = pca.explained_variance_ratio_[0]
# calculate the percentage of the variance contained in the first principal component

print(w, v)

print(var)
