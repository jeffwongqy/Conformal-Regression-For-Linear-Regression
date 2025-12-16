import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.datasets import make_regression

# generate sample
X, y = make_regression(n_samples = 1000, n_features = 5, noise = 10, random_state = 42)

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# set parameters
alpha = 0.1 
n_bootstrap = 100

# store residuals
residuals = []

# bootstrap conformal prediction
for i in range(n_bootstrap):
    # bootstrap resample
    X_res, y_res = resample(X_train, y_train, replace = True, random_state = 42)

    # fit model
    model = LinearRegression()
    model.fit(X_res, y_res)

    # prediction 
    y_pred = model.predict(X_train)

    # compute absolute residuals
    residuals.extend(np.abs(y_train - y_pred))

# compute global quantiles
q = np.quantile(residuals, 1 - alpha)

# fit final model on full training set
final_model = LinearRegression()
final_model.fit(X_train, y_train)

# prediction on test set
y_test_pred = final_model.predict(X_test)

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

