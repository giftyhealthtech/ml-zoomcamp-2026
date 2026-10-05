# Week 2: Regression

This week focused on **Regression** and using machine learning to predict a continuous target variable.

I worked with the 2026 Car Fuel Efficiency dataset and built regression models from scratch using NumPy, rather than relying entirely on scikit-learn.

## Topics

* Regression and predicting continuous values
* Exploratory Data Analysis (EDA)
* Train/validation/test split
* Linear Regression
* RMSE (Root Mean Squared Error)
* Handling missing values
* Mean imputation
* Regularized Linear Regression
* Effect of different regularization values (`r`)
* Effect of random seeds on model performance
* Combining training and validation data for final training
* Evaluating the final model on the test set

## Practical Work

The goal of the project was to predict `fuel_efficiency_mpg` using:

* `engine_displacement`
* `horsepower`
* `vehicle_weight`
* `model_year`

I implemented linear regression from scratch using the normal equation and evaluated the predictions using RMSE.

I also experimented with different approaches to missing values and compared their validation performance.

For regularized linear regression, I tested:

```text
[0, 0.01, 0.1, 1, 5, 10, 100]
```

and compared their RMSE scores on the validation set.

I also investigated how changing the random seed affects the validation score and used the results to understand model stability.

Finally, after selecting the approach based on the validation results, I combined the training and validation data and evaluated the final model on the test set.

##  Homework

This folder contains the Week 2 homework from DataTalksClub.
* Questions are provided in [`homework.md`](homework.md)
* My solutions are provided in [`homework.ipynb`](homework.ipynb)

## Key Things I Learned

Since I already had experience with linear regression, this week was mainly about **refreshing my knowledge and strengthening my understanding of the concepts behind it**.

* I refreshed how to implement **linear regression manually using the normal equation**, rather than relying on a library implementation.
* I revisited **regularization** and got a clearer understanding of how the regularization parameter `r` affects the model.
* One important thing I clarified was that **not all assumptions of linear regression need to be checked before building the model**. Some are assessed after fitting the model, particularly through the behavior of the residuals.
* I strengthened my understanding of **model evaluation and validation**, particularly the importance of using separate training, validation, and test sets.
* I revisited how **different random seeds can affect validation results**. reinforcing the idea that a single train/validation split provides only one view of model performance.
* I reinforced the importance of keeping the **test set completely separate** until the final evaluation, especially when making model or hyperparameter choices.

## Results

The best regularization value on the validation set was `r = 0`,
with a validation RMSE of `2.20529319475341`.

After retraining on the combined training and validation data,
the final test RMSE was `2.236`.