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

## **Cross-Validation Conformal Regression:**
Cross-validation conformal regression extends conformal prediction by using K-Fold Cross Validation instead of a single calibration split. The dataset is divided into K folds, and for each fold, a regression model is trained on the remaining K-1 folds and used to predict the left-out fold. This ensures that every data points receives an out-of-fold prediction from a model that was not trained on it. 

The absolute residuals from all folds are then pooled together to estimate a global error distribution. A quantile of these residuals, based on a chosen significance level $\alpha$, is used to construct prediction intervals around the out-of-fold predictions. These intervals provide distribution-free uncertainty estimates and achieve approximately $1-\alpha$ empirical coverage while efficienctly using the entire dataset. 

## **Important Metrics used in Conformal Regression**
1. Empirical Coverage - measures the proportion of true target values that fall within the prediction intervals. It indicates how reliable the intervals are and should be close to the nominal confidence level $1-\alpha$

2. Average Interval Length (or Width) - Computes the average width of the prediction intervals. It reflects the uncertainty of the predictions - shorter intervals are preferred as long as the desired coverage is maintained. 

3. Significance Level $(\alpha)$ - controls the confidence levels of the prediction intervals. A smaller $\alpha$ produces wider intervals with higher coverage, while a larger $\alpha$ yields narrower intervals. 