# Week 3: Classification

This week focused on **Classification** and using machine learning to predict categorical outcomes.

I worked with the 2026 Lead Scoring dataset and built a classification workflow using Python, Pandas, and Scikit-learn to predict whether a lead would convert (`converted`) or not.

## Topics

* Classification and predicting categorical outcomes
* Exploratory Data Analysis (EDA)
* Handling missing values
* Mode and correlation analysis
* Train/validation/test split
* Mutual information for feature selection
* One-hot encoding of categorical variables
* Logistic Regression
* Accuracy as a classification evaluation metric
* Feature elimination and feature importance
* Regularization in Logistic Regression
* Effect of different regularization strengths (`C`)
* Model evaluation using validation data

## Practical Work

The goal of this project was to predict whether a lead would convert to a customer using the 2026 Lead Scoring dataset.

The target variable was:

* `converted` — whether the lead signed up for the platform.

I started by exploring the dataset, checking its data types, examining unique values, and identifying missing values. I handled missing values by replacing them with `'NA'` for categorical features and `0.0` for numerical features.

I then explored the data by identifying the most frequent value in the `industry` column and calculating the correlation matrix for the numerical features.

For model development, I split the dataset into training, validation, and test sets using the specified random seed. I kept the target variable separate from the input features.

I calculated **mutual information scores** to investigate the relationship between the categorical features and the target variable, using the training set only.

Next, I trained a **Logistic Regression model**. I used one-hot encoding to represent categorical variables numerically and evaluated the model using accuracy on the validation set.

I also applied feature elimination by removing individual features and comparing the resulting validation accuracy with the baseline model. This helped me investigate how much each feature contributed to the model's predictive performance.

Finally, I experimented with different values of the regularization parameter `C` to examine how regularization affects the model's performance.

## Homework

This folder contains the Week 3 homework from DataTalksClub.

* Questions are provided in [`homework.md`](homework.md).
* My solutions are provided in [`homework.ipynb`](homework.ipynb).

## Key Things I Learned

Since I already had some machine learning experience, this week was mainly about **refreshing my understanding of classification and strengthening my practical model evaluation skills**.

* I revisited **Logistic Regression** as a classification algorithm and practised using it to predict categorical outcomes.
* I reinforced my understanding of **one-hot encoding** and how categorical variables can be represented for machine learning models.
* I explored **mutual information** as a way to measure the statistical dependency between categorical features and a target variable.
* I practised using **accuracy to evaluate classification models** on validation data.
* I explored **feature elimination** by comparing model performance with and without individual features.
* I revisited **regularization** and how the parameter `C` controls the strength of regularization in Scikit-learn's Logistic Regression.
* I reinforced the importance of keeping the **training, validation, and test sets separate** to prevent data leakage and obtain a more reliable evaluation.