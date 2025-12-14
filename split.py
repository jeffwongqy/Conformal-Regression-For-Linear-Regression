import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# generate sample 
X, y = make_regression(n_samples = 1000, n_features = 5, noise = 10, random_state = 42)

# split data into train and calibration sets
X_train, X_test_calib, y_train, y_test_calib = train_test_split(X, y, test_size = 0.2, random_state = 42)
X_test, X_calib, y_test, y_calib = train_test_split(X_test_calib, y_test_calib, test_size = 0.5, random_state = 42)

# fit linear regression on train set
model = LinearRegression()
model.fit(X_train, y_train)

# predict on calibration set
y_calib_pred = model.predict(X_calib)

# compute residuals
residuals = np.abs(y_calib - y_calib_pred)

# set 90% significance level
alpha = 0.1

# find the quantile of residuals
q = np.quantile(residuals, 1 - alpha)

# predict on test set
y_test_pred = model.predict(X_test)

# compute prediction intervals
lower = y_test_pred - q
upper = y_test_pred + q

# store all values into the dataframe
results_df = pd.DataFrame({'predictions': y_test_pred, 
                           'lower bounds': lower, 
                           'upper bounds': upper})
print(results_df)

# average length of intervals
avg_length = np.mean(upper - lower)

print("Average length of intervals: ",avg_length)

# empirical coverage
coverage = np.mean((y_test >= lower) & (y_test <= upper))
print("Empirical coverage: ", coverage)





