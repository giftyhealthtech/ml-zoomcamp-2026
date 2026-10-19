# Week 4: Evaluation Metrics

This week focused on **evaluating classification models** and understanding how different metrics help measure predictive performance.

Building on Week 3, I continued working with the 2026 Lead Scoring dataset and a Logistic Regression model to predict whether a lead would convert (`converted`) or not.

Using Python, Pandas, NumPy, Matplotlib, and Scikit-learn, I explored classification evaluation metrics, decision thresholds, cross-validation, and hyperparameter tuning.

## Topics Covered

- ROC AUC (Receiver Operating Characteristic — Area Under the Curve)
- ROC AUC for numerical feature importance
- Logistic Regression
- One-hot encoding with `DictVectorizer`
- Classification thresholds
- Precision and Recall
- Precision–Recall trade-offs
- F1 score
- Five-fold cross-validation
- Standard deviation of evaluation scores
- Hyperparameter tuning
- Regularization strength (`C`)
- Model evaluation and comparison

## Practical Work

The goal of this project was to evaluate a classification model that predicts whether a lead converts to a customer using the 2026 Lead Scoring dataset.

The target variable was:

- `converted` — whether the lead signed up for the platform.

### Data Preparation

I inspected the dataset to understand its structure, data types, and missing values. I replaced missing categorical values with `'NA'` and missing numerical values with `0.0`.

I then split the dataset into training, validation, and test sets using the specified `train_test_split` configuration and random seed.

### ROC AUC and Feature Importance

I calculated ROC AUC scores for selected numerical features to examine how well each feature could distinguish between converted and non-converted leads.

The features evaluated were:

- `lead_score`
- `number_of_courses_viewed`
- `interaction_count`
- `annual_income`

For features with an AUC below 0.5, I reversed the score direction to examine the corresponding AUC in the opposite direction.

### Logistic Regression and ROC AUC Evaluation

I applied one-hot encoding using Scikit-learn's `DictVectorizer` and trained a Logistic Regression classifier with the following parameters:

- Solver: `liblinear`
- Regularization strength (`C`): `1.0`
- Maximum iterations: `1000`

I evaluated the model on the validation dataset using ROC AUC and predicted probabilities rather than relying only on classification accuracy.

### Precision and Recall

I evaluated precision and recall across classification thresholds from `0.00` to `1.00`, using increments of `0.01`.

I plotted both metrics to visualize how changing the classification threshold affects the balance between identifying positive cases and avoiding false positives.

I also identified the threshold at which precision and recall were closest to each other.

### F1 Score

I calculated the F1 score across the same classification thresholds.

The F1 score combines precision and recall into a single metric, helping evaluate their balance. I identified the threshold that maximized the F1 score on the validation data.

### Five-Fold Cross-Validation

I used Scikit-learn's `KFold` with five splits, shuffling enabled, and `random_state=1` to evaluate the Logistic Regression model across different training and validation folds.

I calculated the ROC AUC score for each fold and examined the standard deviation of the scores to understand the consistency of model performance across the folds.

### Hyperparameter Tuning

I used five-fold cross-validation to compare three values of the Logistic Regression regularization parameter:

- `C = 0.000001`
- `C = 0.001`
- `C = 1`

For each value, I calculated the mean ROC AUC and standard deviation across the five folds.

This allowed me to compare model performance and identify the regularization setting with the best mean ROC AUC, applying the specified tie-breaking rules when necessary.

## Homework

This folder contains my Week 4 homework from DataTalksClub.

- Questions: [`homework.md`](homework.md)
- Solutions: [`homework.ipynb`](homework.ipynb)

## What I Learned

This week helped me deepen my understanding of classification evaluation beyond accuracy.

- I learned how ROC AUC can evaluate a model's ability to distinguish between positive and negative classes.
- I practised using individual numerical features as scores to assess their discriminatory power.
- I explored how classification thresholds affect precision and recall.
- I learned how the F1 score combines precision and recall and how to identify a threshold that maximizes it.
- I practised using five-fold cross-validation to evaluate model performance across multiple data splits.
- I used standard deviation to examine the variability of evaluation scores across folds.
- I compared different regularization strengths using cross-validation and mean ROC AUC.
- I strengthened my debugging skills by checking notebook execution order and rerunning cells to ensure that evaluation results were consistent.

## Conclusion

Week 4 strengthened my ability to evaluate classification models using multiple metrics rather than relying on a single performance measure.

Through threshold analysis, F1 score optimization, cross-validation, and hyperparameter tuning, I gained more practical experience in assessing model performance and comparing model configurations.

This work builds on my Week 3 classification project and provides a stronger foundation for developing and evaluating machine learning models.

## Acknowledgements

Thanks to [DataTalksClub](https://github.com/DataTalksClub) for the Machine Learning Zoomcamp curriculum and practical exercises.

Course repository: https://github.com/DataTalksClub/machine-learning-zoomcamp
