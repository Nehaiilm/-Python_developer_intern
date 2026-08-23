# Data Analysis Task

Beginner-level Python internship task: analyze student exam scores using pandas
and visualize the results with matplotlib.

## Files
- `student_data.csv` — raw dataset (20 students, 5 subjects)
- `task.py` — loads the data, computes statistics, ranks students, saves outputs
- `processed_student_data.csv` — dataset with an added `Average_Score` column, sorted by rank
- `average_scores.png` — bar charts of subject-wise and student-wise average scores
- `Report.docx` — write-up of objective, methodology, findings, and conclusion

## How to run
```bash
pip install pandas matplotlib
python task.py
```

## What it does
1. Loads `student_data.csv` into a pandas DataFrame and checks for missing values
2. Computes subject-wise summary statistics (mean, std, min, max)
3. Calculates each student's average score and ranks them
4. Calculates the class average per subject
5. Saves the ranked dataset to `processed_student_data.csv`
6. Generates and saves `average_scores.png`
