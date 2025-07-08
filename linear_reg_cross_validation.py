import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score

nba = pd.read_csv("nbaallelo_slr.csv")

# Create a new column in the data frame that is the difference between pts and opp_pts
nba['y'] = nba['pts'] - nba['opp_pts']

# Split the data into training and test sets
train, test = train_test_split(nba, test_size=0.30, random_state=0)

# Store relevant columns as variables
X = train[['elo_i']]
y = train[['y']]

# Initialize the linear regression model
SLRModel = LinearRegression()
# Fit the model on X and y
SLRModel.fit(X,y)

# Perform 10-fold cross-validation with the default scorer
tenFoldScores = cross_val_score(SLRModel, X, y, cv=10)
print('The cross-validation scores are', tenFoldScores)