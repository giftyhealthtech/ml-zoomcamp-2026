# Week 6: Decision Trees and Ensemble Learning

This week focused on **tree-based machine learning models for regression** and understanding how ensemble methods can improve predictive performance.

Continuing with the car fuel-efficiency dataset, I explored Decision Tree Regression, Random Forest Regression, feature importance, and XGBoost to predict vehicle fuel efficiency (`fuel_efficiency_mpg`).

Using Python, Pandas, NumPy, and Scikit-learn, I trained and evaluated different regression models, experimented with hyperparameters, and compared their performance using Root Mean Squared Error (RMSE).

## Topics Covered

- Decision Tree Regression
- Decision Tree splitting and feature selection
- Random Forest Regression
- Ensemble Learning
- Number of estimators (`n_estimators`)
- Maximum tree depth (`max_depth`)
- Hyperparameter tuning
- Feature importance
- Gradient Boosting
- XGBoost Regression
- Learning rate (`eta`)
- Model evaluation using RMSE

## Practical Work

The goal of this project was to predict car fuel efficiency using the 2026 car fuel-efficiency dataset.

The target variable was:

- `fuel_efficiency_mpg` — the fuel efficiency of a vehicle measured in miles per gallon (MPG).

### Data Preparation

I loaded the dataset using Pandas and inspected its structure, data types, and descriptive statistics.

I replaced missing values with `0.0` and split the dataset into training, validation, and test sets using the specified `train_test_split` configuration and random seed.

I also used Scikit-learn's `DictVectorizer` to convert the dataframes into numerical feature matrices for model training.

### Decision Tree Regression

I trained a Decision Tree Regressor with `max_depth=1` to predict fuel efficiency.

I examined the resulting tree structure using `export_text()` to identify the feature selected for the initial split.

This helped me understand how decision trees make predictions by splitting data based on feature values.

### Random Forest Regression

I trained a Random Forest Regressor using the following initial configuration:

- Number of estimators: `10`
- Random state: `1`

I evaluated the model on the validation dataset using Root Mean Squared Error (RMSE).

This introduced me to ensemble learning, where multiple decision trees work together to produce predictions.

### Hyperparameter Tuning

I experimented with different values of `n_estimators`:

- `10`
- `50`
- `100`
- `150`

I compared their validation RMSE scores to identify the number of estimators that produced the lowest prediction error.

I also explored the effect of maximum tree depth by testing:

- `max_depth = 10`
- `max_depth = 15`
- `max_depth = 20`
- `max_depth = 25`

For each depth, I evaluated different numbers of estimators and calculated the mean RMSE to determine the best-performing configuration.

### Feature Importance

I explored feature importance using the `feature_importances_` attribute of the Random Forest Regressor.

I compared the importance of selected vehicle features:

- `vehicle_weight`
- `horsepower`
- `acceleration`
- `engine_displacement`

This helped me understand how tree-based models estimate the relative contribution of different features to their predictions.

### XGBoost Regression

I trained regression models using XGBoost with the `reg:squarederror` objective.

I created training and validation `DMatrix` objects and used a watchlist to monitor model performance during training.

I experimented with two learning rates:

- `eta = 0.3`
- `eta = 0.1`

Both models were trained for 100 boosting rounds while keeping the other parameters constant.

I compared their validation RMSE scores to understand how the learning rate affects model performance.

## Homework

This folder contains my Week 6 homework from DataTalksClub.

- Questions: [`homework.md`](homework.md)
- Solutions: [`homework.ipynb`](homework.ipynb)

The homework covered decision tree training, Random Forest evaluation, hyperparameter tuning, feature importance, and XGBoost regression.

## What I Learned

This week expanded my understanding of regression beyond linear models.

- I learned how decision trees split data based on feature values to make predictions.
- I explored ensemble learning and how Random Forest combines multiple decision trees.
- I practised tuning the number of estimators and maximum tree depth to improve model performance.
- I learned how to extract and interpret feature importance from tree-based models.
- I explored XGBoost and its approach to gradient boosting.
- I compared different learning rates and observed their effects on validation performance.
- I strengthened my understanding of RMSE as an evaluation metric for regression problems.
- I gained more experience comparing models systematically using validation data.

## Conclusion

Week 6 gave me practical experience with tree-based regression models and ensemble learning techniques.

By experimenting with Decision Trees, Random Forests, and XGBoost, I gained a better understanding of how different algorithms approach regression problems and how hyperparameter tuning can influence predictive performance.

This week's work builds on my previous regression and classification exercises and broadens my understanding of machine learning model development and evaluation.

## Acknowledgements

Thanks to [DataTalksClub](https://github.com/DataTalksClub) for the Machine Learning Zoomcamp curriculum and practical exercises.

Course repository: https://github.com/DataTalksClub/machine-learning-zoomcamp