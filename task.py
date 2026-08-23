"""
Data Analysis Task - Python Developer Internship
--------------------------------------------------
Loads student score data, performs exploratory analysis with pandas,
and visualizes average scores per subject and per student.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# 1. Load the dataset
# ----------------------------------------------------------------------
df = pd.read_csv("student_data.csv")
subjects = ["Math", "Science", "English", "Computer_Science", "Social_Studies"]

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values per column:\n", df.isnull().sum())

# ----------------------------------------------------------------------
# 2. Summary statistics
# ----------------------------------------------------------------------
summary_stats = df[subjects].describe().T[["mean", "std", "min", "max"]]
summary_stats.rename(columns={"mean": "Average", "std": "Std_Dev",
                               "min": "Min", "max": "Max"}, inplace=True)
print("\nSubject-wise summary statistics:\n", summary_stats.round(2))

# ----------------------------------------------------------------------
# 3. Per-student average score (adds a new column)
# ----------------------------------------------------------------------
df["Average_Score"] = df[subjects].mean(axis=1).round(2)
df_sorted = df.sort_values("Average_Score", ascending=False).reset_index(drop=True)
print("\nStudents ranked by average score:\n",
      df_sorted[["Student_Name", "Average_Score"]])

top_student = df_sorted.iloc[0]
print(f"\nTop performer: {top_student['Student_Name']} "
      f"({top_student['Average_Score']} avg)")

# ----------------------------------------------------------------------
# 4. Per-subject class average
# ----------------------------------------------------------------------
subject_avg = df[subjects].mean().round(2)
print("\nClass average per subject:\n", subject_avg)

# ----------------------------------------------------------------------
# 5. Save processed results
# ----------------------------------------------------------------------
df_sorted.to_csv("processed_student_data.csv", index=False)

# ----------------------------------------------------------------------
# 6. Visualization -> average_scores.png
# ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# (a) Class average per subject
axes[0].bar(subject_avg.index, subject_avg.values, color="#4C72B0")
axes[0].set_title("Class Average Score by Subject")
axes[0].set_ylabel("Average Score")
axes[0].set_ylim(0, 100)
axes[0].tick_params(axis="x", rotation=30)
for i, v in enumerate(subject_avg.values):
    axes[0].text(i, v + 1, str(v), ha="center", fontsize=9)

# (b) Top 10 students by average score
top10 = df_sorted.head(10)
axes[1].barh(top10["Student_Name"][::-1], top10["Average_Score"][::-1],
             color="#55A868")
axes[1].set_title("Top 10 Students by Average Score")
axes[1].set_xlabel("Average Score")
axes[1].set_xlim(0, 100)

plt.tight_layout()
plt.savefig("average_scores.png", dpi=150)
print("\nSaved chart to average_scores.png")
