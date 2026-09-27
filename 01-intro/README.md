# Week 1 — Introduction to Machine Learning

This folder contains my Week 1 coursework and homework solutions for the [DataTalksClub Machine Learning Zoomcamp 2026](https://github.com/DataTalksClub/machine-learning-zoomcamp "DataTalksClub Machine Learning Zoomcamp").

##  Topics
* Introduction to Machine Learning
* Machine Learning terminology
* Supervised learning
* CRISP-DM
* Model selection
* Basic Machine Learning concepts

##  Homework
This folder contains the Week 1 homework from DataTalksClub.
* Questions are provided in [`homework.md`](homework.md)
* My solutions are provided in [`homework.ipynb`](homework.ipynb)

## Key Things I Learned

* **Pandas Foundations:** Refreshed my understanding of filtering and selecting columns in Pandas using the syntax:
  ```python
  df[filter][columns]
  ```
* **Linear Algebra Basics:** Refreshed the difference between dot product and element-wise multiplication.
* **Matrix Inversion:** Learned how to invert a matrix using NumPy:
  ```python
  np.linalg.inv()
  ```
* **Inverse Matrix Requirements:** Reviewed the requirements for a matrix to have an inverse:
  * The matrix must be **square** (same number of rows and columns).
  * The determinant must be **non-zero**.
* **Handling Singular Matrices:** Learned about alternatives when a matrix cannot be directly inverted:
  * **Pseudo-inverse** using `np.linalg.pinv()`
  * **L2 regularization**, which can help make matrix calculations more stable when dealing with singular or ill-conditioned matrices.
* **NumPy Practice:** Practiced using NumPy for matrix operations, including:
  * Matrix transpose
  * Matrix multiplication
  * Matrix inversion
  * Solving for weights

## Resources
* [DataTalksClub Machine Learning Zoomcamp Course Repository](https://github.com/DataTalksClub/machine-learning-zoomcamp "DataTalksClub Machine Learning Zoomcamp")