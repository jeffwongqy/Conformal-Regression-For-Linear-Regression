import numpy as np 
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# generate sample data
X, y = make_regression(n_samples = 1000, n_features = 5, noise = 10, random_state = 42)

# set the k-fold parameters
kf = KFold(n_splits = 5, shuffle = True, random_state = 42)

# initialize empty lower, upper, y_pred for prediction intervals
y_oof_pred = np.zeros(len(y))
residuals_all = []

# cross-validation conformal prediction 
for train_index, val_index in kf.split(X):
    X_tr, X_val = X[train_index], X[val_index]
    y_tr, y_val = y[train_index], y[val_index]

    # fit the model
    model = LinearRegression()
    model.fit(X_tr, y_tr)

    # predict on validation fold
    y_val_pred = model.predict(X_val)

    # store the prediction results at correct indices and residuals all 
    y_oof_pred[val_index] = y_val_pred
    residuals_all.extend(np.abs(y_val - y_val_pred))

# compute global conformal prediction 
alpha = 0.1
q_cv = np.quantile(residuals_all, 1 - alpha)

# prediction intervals
lower = y_oof_pred - q_cv
upper = y_oof_pred + q_cv

# store all values into the dataframe
results_df = pd.DataFrame({'predictions': y_oof_pred, 
                           'lower bounds': lower, 
                           'upper bounds': upper})
print(results_df)

# average length of intervals
avg_length = np.mean(upper - lower)

print("Average length of intervals: ",avg_length)

# empirical coverage
coverage = np.mean((y >= lower) & (y <= upper))
print("Empirical coverage: ", coverage)