# Framingham Heart Study
Data used in this project is a subset of the Framingham Heart Study started in 1948. This project analyzes how physiological variables like weight, cholesterol, and smoking habits relate to high blood pressure (hypertension) and coronary heart disease (CHD), using logistic and linear regression.

[Link to code](2.Fram-regression/project_notebook_regression_analysis.ipynb)

[Link to output](2.Fram-regression/Output)

## Methods
1. Rescaling
   - Numerical variables are rescaled using standard deviation scaling for making the model more meaningful.
   - All interactions are calculated on the rescaled variables.

2. Linear regression for systolic blood pressure
   - Multiple regression models are built with increasing complexity.
   - Interaction terms are added (e.g., sFRW:sAGE) to account for how the relationship between variables changes with age, sex, or other factors.

3. Logistic regression for hypertension
4. Logistic regression for CHD
3 and 4 involve the creation of binary variables and the fitting of S-curves to account for the binary nature of the data.

## Tools used
Python with numpy and pandas for data analysis, statsmodels and matplotlib for modelling and plotting

## What did I learn?
- Interaction terms are important: Fitting a model only with independent factors often misses how these effects work together. For example, weight is a stronger predictor of high BP in older people.
- Data standardization is crucial: Scaling features by their standard deviation (divided by 2) made regression coefficients easier to interpret, especially when interactions were involved.
