
# Python Developer Internship

This repository contains the projects completed during my Python Developer
Internship, covering data analysis, numerical computation, and applied
machine learning using Python.

**Author:** Neha Sinha
**Roll No.:** CS-2341460
**B.Tech CSE, IILM University** — Semester 7, Section 4CSE12

---

## Repository Structure

```
Python_developer_intern/
│
├── Data_Analysis_task/
│   ├── task.py
│   ├── student_data.csv
│   ├── processed_student_data.csv
│   ├── average_scores.png
│   ├── Report.docx
│   └── README.md
│
├── Matrix_Operations_Tool/
│   ├── matrix_tool.py
│   └── README.md
│
├── linear_regression/
│   ├── linear_regression.py
│   ├── house_data.csv
│   ├── predictions.csv
│   ├── house_price_prediction.png
│   ├── Report.docx
│   └── README.md
│
└── README.md   (this file)
```

---


## 1. Data Analysis Task

**Goal:** Explore a dataset of student scores and summarize performance
using pandas.

- Loads `student_data.csv` (20 students × 5 subjects)
- Computes subject-wise mean, standard deviation, min, and max
- Derives each student's average score and ranks them
- Saves results to `processed_student_data.csv`
- Visualizes subject and student performance in `average_score.png`


---

## 2. Matrix Operations Tool

**Goal:** Build a reusable command-line tool for common matrix operations.

- Interactive menu with 7 operations: Addition, Subtraction, Multiplication,
  Scalar Multiplication, Transpose, Determinant, Inverse
- Validates matrix dimensions and handles errors (mismatched shapes,
  non-square matrices, singular matrices) with clear messages


---

## 3. Linear Regression — House Price Prediction

**Goal:** Train and evaluate a supervised machine learning model to
predict house prices.

- Loads `house_data.csv` (200 houses, 5 features)
- Splits data 80/20 into training and test sets
- Trains a `LinearRegression` model with scikit-learn
- Evaluates using MAE, RMSE, and R² score (achieved R² = 0.9966)
- Saves predictions to `predictions.csv` and a results chart to
  `house_price_prediction.png`


---

## Tools & Technologies

- **Language:** Python 3
- **Libraries:** pandas, NumPy, matplotlib, scikit-learn
- **Environment:** Visual Studio Code
- **Version Control:** Git & GitHub

---


