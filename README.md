# Conformal Regression for Linear Regression 

## **Aim:**
To develop a reliable regression model that provides not only point predictions but also valid predictio intervals, using conformal prediction methods to quantify uncertainty. 

## **Objectives:**
- To implement linear regression models on a synthetic dataset using train-test split and cross-validation.
- To apply conformal prediction techniques to generate distribution-free prediction intervals.
- To evaluate the performance of the prediction intervals using empirical coverage and average interval length. 
- To compare the effectiveness of split conformal and cross-validation conformal approaches. 

## **Split Conformal Regression:**
Split conformal regression is a distribution-free method used to quantify uncertainty in regression predictions. The dataset is first split into **three parts**: a training set, a calibration set, and a test set. The regression model is trained only on the training set. It is then used to make predictions on the calibration set, where absolute residuals (differences between true and predicted values) are computed. 

These residuals are used to estimate a **quantile threshold** based on a chosen significance level $\alpha$. This threshold represents how large the prediction error typically is. When making predictions on new test data, the model's point predictions are expanded by this threshold to form **prediction intervals**. 

The resulting intervals are guaranteed, under minimal assumptions, to contain the true target value with probability approximately $1 - \alpha$. The quality of these intervals is evaluated using empirical coverage (how often the true values fall inside the intervals) and average interval length (how wide the intervals are).